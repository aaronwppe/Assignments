-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 18, 2024 at 08:30 PM
-- Server version: 10.11.10-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `u333757828_group1_b`
--

-- --------------------------------------------------------

--
-- Table structure for table `aaron_book_taken`
--

CREATE TABLE `aaron_book_taken` (
  `id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  `date_taken` date NOT NULL,
  `status` enum('taken','returned','overdue') NOT NULL DEFAULT 'taken'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `aaron_book_taken`
--

INSERT INTO `aaron_book_taken` (`id`, `book_id`, `member_id`, `date_taken`, `status`) VALUES
(15, 3, 1, '2024-11-01', 'taken'),
(16, 4, 2, '2024-11-02', 'returned'),
(17, 5, 3, '2024-11-03', 'taken'),
(18, 6, 4, '2024-11-04', 'overdue'),
(19, 7, 5, '2024-11-05', 'taken'),
(20, 4, 3, '2024-11-06', 'taken'),
(21, 5, 1, '2024-11-07', 'returned'),
(22, 3, 2, '2024-11-08', 'overdue'),
(23, 4, 5, '2024-11-09', 'taken'),
(24, 5, 4, '2024-11-10', 'taken'),
(25, 6, 1, '2024-11-11', 'returned'),
(26, 7, 3, '2024-11-12', 'taken'),
(27, 5, 2, '2024-11-13', 'taken'),
(28, 3, 4, '2024-11-14', 'returned'),
(29, 7, 1, '2024-11-15', 'overdue'),
(30, 4, 3, '2024-11-16', 'returned'),
(31, 6, 2, '2024-11-17', 'taken'),
(32, 3, 3, '2024-11-19', 'taken'),
(33, 3, 5, '2024-11-19', 'returned');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `aaron_book_taken`
--
ALTER TABLE `aaron_book_taken`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `aaron_book_taken`
--
ALTER TABLE `aaron_book_taken`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
