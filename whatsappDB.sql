-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 06, 2021 at 08:17 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `whatsapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `id` int(11) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `url` varchar(250) NOT NULL,
  `is_approved` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`id`, `phone`, `url`, `is_approved`) VALUES
(1, '919028788974', 'https://wa1.s3.amazonaws.com/2021-01-24--919028788974.jpg?AWSAccessKeyId=AKIAILR3LKZCMYH4SMQQ', 1),
(2, '917744994714', 'https://wa1.s3.amazonaws.com/2021-01-25--917744994714.jpg?AWSAccessKeyId=AKIAILR3LKZCMYH4SMQQ', 1),
(3, '919028788974', 'https://wa1.s3.amazonaws.com/2021-01-26--919028788974.jpg?AWSAccessKeyId=AKIAILR3LKZCMYH4SMQQ', 1),
(4, '917028987266', 'https://wa1.s3.amazonaws.com/2021-01-28--917028987266.jpg?AWSAccessKeyId=AKIAILR3LKZCMYH4SMQQ', 1),
(5, '917744994714', 'https://wa1.s3.amazonaws.com/2021-01-28--917744994714.jpg?AWSAccessKeyId=AKIAILR3LKZCMYH4SMQQ', 1),
(6, '919769984145', 'https://wa1.s3.amazonaws.com/2021-01-28--919769984145.jpg?AWSAccessKeyId=AKIAILR3LKZCMYH4SMQQ', 1),
(7, '918788467838', 'https://wa1.s3.amazonaws.com/2021-03-06--918788467838.jpg?AWSAccessKeyId=AKIAILR3LKZCMYH4SMQQ', 1),
(8, '919156591432', 'https://wa1.s3.amazonaws.com/2021-03-06--919156591432.jpg?AWSAccessKeyId=AKIAILR3LKZCMYH4SMQQ', 1),
(9, '917744994714', 'https://wa1.s3.amazonaws.com/2021-03-06--917744994714.jpg?AWSAccessKeyId=AKIAILR3LKZCMYH4SMQQ', 1),
(10, '919158133624', 'https://wa1.s3.amazonaws.com/2021-03-06--919158133624.jpg?AWSAccessKeyId=AKIAILR3LKZCMYH4SMQQ', 1),
(11, '919823495053', 'https://wa1.s3.amazonaws.com/2021-03-06--919823495053.jpg?AWSAccessKeyId=AKIAILR3LKZCMYH4SMQQ', 1),
(12, '917744994714', 'https://wa1.s3.amazonaws.com/2021-03-06--917744994714.jpg?AWSAccessKeyId=AKIAILR3LKZCMYH4SMQQ', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user_details`
--
ALTER TABLE `user_details`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user_details`
--
ALTER TABLE `user_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
