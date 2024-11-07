from mysql import connector
import switch
from prettytable import PrettyTable

query = {
    'book_taken': {
        'insert': 'INSERT INTO aaron_book_taken(book_id, member_id, date_taken, status) VALUES(%s, %s, %s, %s)',
    }
}


class Book:
    def __init__(self):
        self.table = PrettyTable(['ID', 'Name', 'Author', 'Published(Year)'])
        self.query = {
            'select': 'SELECT * FROM aaron_book',
            'insert': 'INSERT INTO aaron_book(name, author, year_of_publication) VALUES(%s, %s, %s)',
            'get_book_id': 'SELECT id FROM aaron_book WHERE name = %s',
        }

    def get_id(self, cursor, name):
        cursor.execute(self.query['get_book_id'], (name, ))
        result = cursor.fetchone()

        if not result:
            return None

        return result[0]

    def get_table(self, cursor):
        cursor.execute(self.query['select'])
        result = cursor.fetchall()

        self.table.clear_rows()
        self.table.add_rows([list(row) for row in result])

        return self.table

    def add(self, cursor, connection):
        name = input('Book Name: ')
        author = input('Author Name: ')
        year = input('Year Published: ')

        try:
            cursor.execute(self.query['insert'], (name, author, year))
            connection.commit()
            return 'New Book Added!'
        except Exception as e:
            connection.rollback()
            return f'ERROR: Book could not be added!'


class Member:
    def __init__(self):
        self.table = PrettyTable(['ID', 'Name', 'Address', 'Mobile Number'])
        self.query = {
            'select': 'SELECT * FROM aaron_member',
            'insert': 'INSERT INTO aaron_member(name, address, mobile_number) VALUES(%s, %s, %s)',
            'get_member_id': 'SELECT id FROM aaron_member WHERE name = %s'
        }

    def get_id(self, cursor, name):
        cursor.execute(self.query['get_member_id'], (name, ))
        result = cursor.fetchone()

        if not result:
            return None

        return result[0]

    def get_table(self, cursor):
        cursor.execute(self.query['select'])
        result = cursor.fetchall()

        self.table.clear_rows()
        self.table.add_rows([list(row) for row in result])

        return self.table

    def add(self, cursor, connection):
        name = input('Member Name: ')
        address = input('Home Address: ')
        phone = input('Mobile Number: ')

        try:
            cursor.execute(self.query['insert'], (name, address, phone))
            connection.commit()
            return 'New Member Added!'
        except Exception as e:
            connection.rollback()
            return f'ERROR: Member could not be added!'


class BookTaken:
    def __init__(self):
        self.status_tuple = ('taken', 'returned', 'overdue')
        self.table = PrettyTable(['Member', 'Book', 'Date Issued', 'Status'])
        self.query = {
            'select': 'SELECT '
                      'm.name, b.name, date_taken, status '
                      'FROM aaron_book_taken bt '
                      'JOIN aaron_member m ON bt.member_id = m.id '
                      'JOIN aaron_book b ON bt.book_id = b.id ',

            'insert': 'INSERT INTO aaron_book_taken(book_id, member_id, date_taken, status) VALUES(%s, %s, %s, %s)',

            'update_status': 'UPDATE aaron_book_taken SET status = %s WHERE book_id = %s AND member_id = %s;'
        }

    def get_table(self, cursor):
        cursor.execute(self.query['select'])
        result = cursor.fetchall()

        self.table.clear_rows()
        self.table.add_rows([list(row) for row in result])

        return self.table

    @staticmethod
    def get_ids(cursor):
        member_name = input('Member Name: ')
        member_id = Member().get_id(cursor, member_name)
        if not member_id:
            return 'ERROR: Member does not exist!'

        book_name = input('Book Name: ')
        book_id = Book().get_id(cursor, book_name)
        if not book_id:
            return 'ERROR: Book does not exist!'

        return member_id, book_id

    def add(self, cursor, connection):
        ret = self.get_ids(cursor)
        if ret is str:
            return ret

        member_id, book_id = ret

        date = input('Date Issued: ')

        status = input(f'Status{self.status_tuple}: ')
        if status not in self.status_tuple:
            return 'ERROR: Invalid Status provided!'

        try:
            cursor.execute(self.query['insert'], (book_id, member_id, date, status))
            connection.commit()
            return 'New Book Issue Entry Added!'
        except Exception as e:
            connection.rollback()
            return f'ERROR: Book Issue Entry could not be added!'

    def change_status(self, cursor, connection):
        ret = self.get_ids(cursor)
        if ret is str:
            return ret

        member_id, book_id = ret

        status = input(f'Change status to {self.status_tuple}: ')
        if status not in self.status_tuple:
            return 'ERROR: Invalid Status provided!'

        try:
            cursor.execute(self.query['update_status'], (status, book_id, member_id))
            connection.commit()
            return 'Book Issue status changed!'
        except Exception as e:
            connection.rollback()
            return f'ERROR: Book Issue status could not be updated!'


def open_connection():
    connection = connector.connect(host='194.59.164.14',
                                   user='u333757828_group1_b',
                                   database='u333757828_group1_b',
                                   password='9zvUR:a4')
    cursor = connection.cursor()

    return connection, cursor


switch = switch.Switch2()
book = Book()
member = Member()
issue = BookTaken()

switch.add_case('Display all Books', lambda: book.get_table(cur))
switch.add_case('Display all Members', lambda: member.get_table(cur))
switch.add_case('Display all Books Issued', lambda: issue.get_table(cur))
switch.add_case('Add New Book', lambda: book.add(cur, conn))
switch.add_case('Add New Member', lambda: member.add(cur, conn))
switch.add_case('Add New Book Issue Entry', lambda: issue.add(cur, conn))
switch.add_case('Change Status of Issued Book', lambda: issue.change_status(cur, conn))
switch.add_exit_case()

print("Options:")
print(switch.options)

while not switch.exit_is_selected:
    option = input("Perform: ")

    conn, cur = open_connection()
    print(switch.run(option))

    conn.close()
    cur.close()

    print(switch.break_line)
