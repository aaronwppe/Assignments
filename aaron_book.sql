-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 18, 2024 at 08:28 PM
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
-- Table structure for table `aaron_book`
--

CREATE TABLE `aaron_book` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `year_of_publication` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `aaron_book`
--

INSERT INTO `aaron_book` (`id`, `name`, `author`, `year_of_publication`) VALUES
(3, 'Book2', 'his', '2002'),
(4, 'Book abc', 'efgh', '2020'),
(5, 'This book', 'mnop', '2019'),
(6, 'Book 3', 'uvwx', '2018'),
(7, 'Book4', 'cdef', '2021');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `aaron_book`
--
ALTER TABLE `aaron_book`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`,`author`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `aaron_book`
--
ALTER TABLE `aaron_book`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
