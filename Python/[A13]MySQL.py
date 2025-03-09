from mysql import connector
import switch
from prettytable import PrettyTable
import datetime
import re


class DatabaseManager:
    def __init__(self, connection_params):
        self.connection_parameters = connection_params

    def __enter__(self):
        self.connection = connector.connect(**self.connection_parameters)
        self.cursor = self.connection.cursor()

        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is None:
            self.connection.commit()
        else:
            self.connection.rollback()

        self.cursor.close()
        self.connection.close()


class Book:
    query = {
        'select': 'SELECT * FROM aaron_book',
        'insert': 'INSERT INTO aaron_book(name, author, year_of_publication) VALUES(%s, %s, %s)',
        'get_book_id': 'SELECT id FROM aaron_book WHERE name = %s',
        'update_book_name': 'UPDATE aaron_book SET name = %s WHERE id = %s',
        'delete': 'DELETE FROM aaron_book WHERE name = %s',
    }

    def __init__(self, connection_params):
        self.connection_parameters = connection_params

    @classmethod
    def get_empty_table(cls):
        return PrettyTable(['ID', 'Name', 'Author', 'Published(Year)'])

    @classmethod
    def year_is_valid(cls, year):
        try:
            datetime.datetime.strptime(year, '%Y')
            return True
        except ValueError:
            return False


    @classmethod
    def get_id(cls, cursor, name):
        cursor.execute(cls.query['get_book_id'], (name,))
        result = cursor.fetchone()

        if not result:
            return None

        return result[0]

    def get_table(self):
        with DatabaseManager(self.connection_parameters) as cursor:
            cursor.execute(self.query['select'])
            result = cursor.fetchall()

        table = self.get_empty_table()
        table.add_rows([list(row) for row in result])
        # same as below
        # for row in result:
        #     table.add_row(list(row))

        return table

    def add(self):
        name = input('Book Name: ')
        author = input('Author Name: ')

        year = input('Year Published: ')
        if not self.year_is_valid(year):
            return 'ERROR: Invalid Year!'

        with DatabaseManager(self.connection_parameters) as cursor:
            cursor.execute(self.query['insert'], (name, author, year))

        return 'New Book Added!'

    def change_book_name(self):
        name = input('Old Book Name: ')

        with DatabaseManager(self.connection_parameters) as cursor:
            book_id = self.get_id(cursor, name)
            if not book_id:
                return 'ERROR: Book does not exist!'

            new_name = input('New Book Name: ')
            cursor.execute(self.query['update_book_name'], (new_name, book_id))

        return 'Name Changed!'

    def remove(self):
        name = input('Book Name: ')

        with DatabaseManager(self.connection_parameters) as cursor:
            book_id = self.get_id(cursor, name)
            if not book_id:
                return 'ERROR: Book does not exist!'

            t = BookTaken.get_table_by_book_id(cursor, book_id)

            if len(t.rows) != 0:
                print('Corresponding entries of Issued books will also be deleted...')
                print(t)

                confirm = input('Confirm (Y/N) ? ')
                if confirm.lower() == 'n':
                    return 'Book removal failed!'

                if confirm.lower() != 'y':
                    return 'ERROR: Invalid input!'

            BookTaken.remove_by_book_id(cursor, book_id)

            cursor.execute(self.query['delete'], (name,))

        return 'Book removed!'


class Member:
    query = {
        'select': 'SELECT * FROM aaron_member',
        'insert': 'INSERT INTO aaron_member(name, address, mobile_number) VALUES(%s, %s, %s)',
        'get_member_id': 'SELECT id FROM aaron_member WHERE name = %s',
        'delete': 'DELETE FROM aaron_member WHERE name = %s',
    }

    def __init__(self, connection_params):
        self.connection_parameters = connection_params

    @classmethod
    def mobile_is_valid(cls, mobile):
        if re.match(r'^(789)\d{9}$', mobile):
            return True
        else:
            return False

    @classmethod
    def get_empty_table(cls):
        return PrettyTable(['ID', 'Name', 'Address', 'Mobile Number'])

    @classmethod
    def get_id(cls, cursor, name):
        cursor.execute(cls.query['get_member_id'], (name,))
        result = cursor.fetchone()

        if not result:
            return None

        return result[0]

    def get_table(self):
        with DatabaseManager(self.connection_parameters) as cursor:
            cursor.execute(self.query['select'])
            result = cursor.fetchall()

        table = self.get_empty_table()
        table.add_rows([list(row) for row in result])

        return table

    def add(self):
        name = input('Member Name: ')
        address = input('Home Address: ')

        phone = input('Mobile Number: ')
        if not self.mobile_is_valid(phone):
            return 'ERROR: Mobile number invalid!'

        with DatabaseManager(self.connection_parameters) as cursor:
            cursor.execute(self.query['insert'], (name, address, phone))

        return 'New Member Added!'

    def remove(self):
        name = input('Member Name: ')

        with DatabaseManager(self.connection_parameters) as cursor:
            member_id = self.get_id(cursor, name)
            if not member_id:
                return 'ERROR: Member does not exist!'

            t = BookTaken.get_table_by_member_id(cursor, member_id)

            if len(t.rows) != 0:
                print('Corresponding entries of Issued books will also be deleted...')
                print(t)

                confirm = input('Confirm (Y/N) ? ')
                if confirm.lower() == 'n':
                    return 'Member not removed!'

                if confirm.lower() != 'y':
                    return 'ERROR: Invalid input!'

            BookTaken.remove_by_member_id(cursor, member_id)

            cursor.execute(self.query['delete'], (name,))

        return 'Member removed!'


class BookTaken:
    status_tuple = ('taken', 'returned', 'overdue')
    query = {
        'select': 'SELECT '
                  'm.name, b.name, date_taken, status '
                  'FROM aaron_book_taken bt '
                  'JOIN aaron_member m ON bt.member_id = m.id '
                  'JOIN aaron_book b ON bt.book_id = b.id ',

        'select_by_book_id': 'SELECT '
                             'm.name, b.name, date_taken, status '
                             'FROM aaron_book_taken bt '
                             'JOIN aaron_member m ON bt.member_id = m.id '
                             'JOIN aaron_book b ON bt.book_id = b.id '
                             'WHERE bt.book_id = %s ',

        'select_by_member_id': 'SELECT '
                             'm.name, b.name, date_taken, status '
                             'FROM aaron_book_taken bt '
                             'JOIN aaron_member m ON bt.member_id = m.id '
                             'JOIN aaron_book b ON bt.book_id = b.id '
                             'WHERE bt.member_id = %s ',

        'insert': 'INSERT INTO aaron_book_taken(book_id, member_id, date_taken, status) VALUES(%s, %s, %s, %s)',

        'update_status': 'UPDATE aaron_book_taken SET status = %s WHERE book_id = %s AND member_id = %s;',

        'delete': 'DELETE FROM aaron_book_taken WHERE member_id = %s AND book_id = %s ',
        'delete_by_book_id': 'DELETE FROM aaron_book_taken WHERE book_id = %s',
        'delete_by_member_id': 'DELETE FROM aaron_book_taken WHERE member_id = %s',
    }

    def __init__(self, connection_params):
        self.connection_parameters = connection_params

    @classmethod
    def get_empty_table(cls):
        return PrettyTable(['Member', 'Book', 'Date Issued', 'Status'])

    @classmethod
    def status_is_valid(cls, status):
        if status not in cls.status_tuple:
            return False
        else:
            return True

    @classmethod
    def date_is_valid(cls, date):
        try:
            datetime.date.fromisoformat(date)
            return True
        except ValueError:
            return False

    def get_table(self):
        with DatabaseManager(self.connection_parameters) as cursor:
            cursor.execute(self.query['select'])
            result = cursor.fetchall()

        table = self.get_empty_table()
        table.add_rows([list(row) for row in result])

        return table

    @classmethod
    def get_table_by_book_id(cls, cursor, book_id):
        cursor.execute(cls.query['select_by_book_id'], (book_id, ))
        result = cursor.fetchall()

        table = cls.get_empty_table()
        table.add_rows([list(row) for row in result])

        return table

    @classmethod
    def get_table_by_member_id(cls, cursor, member_id):
        cursor.execute(cls.query['select_by_member_id'], (member_id,))
        result = cursor.fetchall()

        table = cls.get_empty_table()
        table.add_rows([list(row) for row in result])

        return table

    @classmethod
    def get_ids(cls, cursor, member_name, book_name):
        member_id = Member.get_id(cursor, member_name)
        if not member_id:
            return 'ERROR: Member does not exist!'

        book_id = Book.get_id(cursor, book_name)
        if not book_id:
            return 'ERROR: Book does not exist!'

        return member_id, book_id

    def add(self):
        member_name = input('Member Name: ')
        book_name = input('Book Name: ')

        with DatabaseManager(self.connection_parameters) as cursor:
            ret = self.get_ids(cursor, member_name, book_name)
            if type(ret) is str:
                return ret

            member_id, book_id = ret

            date = input('Date Issued (YYYY-MM-DD): ')
            if not self.date_is_valid(date):
                return 'ERROR: Invalid date provided!'

            status = input(f'Status{self.status_tuple}: ')
            if not self.status_is_valid(status):
                return 'ERROR: Invalid status provided!'

            cursor.execute(self.query['insert'], (book_id, member_id, date, status))

        return 'New Book Issue Entry Added!'

    def change_status(self):
        member_name = input('Member Name: ')
        book_name = input('Book Name: ')

        with DatabaseManager(self.connection_parameters) as cursor:
            ret = self.get_ids(cursor, member_name, book_name)
            if type(ret) is str:
                return ret

            member_id, book_id = ret

            status = input(f'Change status to {self.status_tuple}: ')
            if status not in self.status_tuple:
                return 'ERROR: Invalid Status provided!'

            cursor.execute(self.query['update_status'], (status, book_id, member_id))

        return 'Book Issue status changed!'

    def remove(self):
        member_name = input('Member Name: ')
        book_name = input('Book Name: ')

        with DatabaseManager(self.connection_parameters) as cursor:
            ret = self.get_ids(cursor, member_name, book_name)
            if type(ret) is str:
                return ret

            cursor.execute(self.query['delete'], (member_name, book_name))

        return 'Book Issue entry removed!'

    @classmethod
    def remove_by_book_id(cls, cursor, book_id):
        cursor.execute(cls.query['delete_by_book_id'], (book_id, ))

    @classmethod
    def remove_by_member_id(cls, cursor, member_id):
        cursor.execute(cls.query['delete_by_member_id'], (member_id,))


class Report:
    query = {
        'book_by_popularity': 'SELECT b.name, COUNT(b.id) AS issue_count FROM aaron_book b '
                              'JOIN aaron_book_taken bt ON b.id = bt.book_id '
                              'GROUP BY b.id ORDER BY issue_count DESC',

        'defaulting_members': 'SELECT m.name, b.name, bt.date_taken FROM aaron_member m '
                              'JOIN aaron_book_taken bt ON bt.member_id = m.id '
                              'JOIN aaron_book b ON b.id = bt.book_id '
                              "WHERE bt.status = 'overdue' "
    }

    def __init__(self, connection_params):
        self.connection_parameters = connection_params

    def list_book_by_popularity(self):
        with DatabaseManager(self.connection_parameters) as cursor:
            cursor.execute(self.query['book_by_popularity'])
            result = cursor.fetchall()

        table = PrettyTable(['Book', 'Number of Times Issued'])
        table.add_rows([list(row) for row in result])

        return table

    def defaulting_members(self):
        with DatabaseManager(self.connection_parameters) as cursor:
            cursor.execute(self.query['defaulting_members'])
            result = cursor.fetchall()

        table = PrettyTable(['Member', 'Overdue Book', 'Date Issued'])
        table.add_rows([list(row) for row in result])

        return table


connection_parameters = {'host': '194.59.164.14',
                         'user': 'u333757828_group1_b',
                         'database': 'u333757828_group1_b',
                         'password': '9zvUR:a4'}

switch = switch.Switch2()
book = Book(connection_parameters)
member = Member(connection_parameters)
issue = BookTaken(connection_parameters)
report = Report(connection_parameters)

switch.add_case('Display all Books', lambda: book.get_table())
switch.add_case('Display all Members', lambda: member.get_table())
switch.add_case('Display all Books Issued', lambda: issue.get_table())

switch.add_case('Add New Book', lambda: book.add())
switch.add_case('Add New Member', lambda: member.add())
switch.add_case('Add New Book Issue Entry', lambda: issue.add())

switch.add_case('Change Book Name', lambda: book.change_book_name())
switch.add_case('Change Status of Issued Book', lambda: issue.change_status())

switch.add_case('Remove Book', lambda: book.remove())
switch.add_case('Remove Member', lambda: member.remove())
switch.add_case('Remove Book Issue Entry', lambda: issue.remove())

switch.add_case('List Books by Popularity', lambda: report.list_book_by_popularity())
switch.add_case('Defaulting Members', lambda: report.defaulting_members())

switch.add_exit_case()

print("Options:")
print(switch.options)

while not switch.exit_is_selected:
    try:
        option = input("Perform: ")
        out_str = switch.run(option)
        print(out_str)
        print(switch.break_line)
    except connector.errors.Error as ex:
        print('ERROR: Operation could not be performed! Database error.')
