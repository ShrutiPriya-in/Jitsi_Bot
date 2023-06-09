-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 09, 2022 at 12:36 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3
create database cbdns;
use cbdns;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";
DROP TABLE tblhr_candidate_meetings;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perfex_crm`
--

-- --------------------------------------------------------

--
-- Table structure for table `tblhr_candidate_meetings`
--

CREATE TABLE `tblhr_candidate_meetings` (
  `id` int(11) NOT NULL,
  `user_id` text NOT NULL,
  `username` varchar(191) NOT NULL,
  `date` varchar(11) NOT NULL,
  `sign_in_time` text DEFAULT NULL,
  `sign_out_time` text DEFAULT NULL,
  `video_cam_on` text DEFAULT NULL,
  `video_cam_off` text DEFAULT NULL,
  `mic_on` text DEFAULT NULL,
  `mic_off` text DEFAULT NULL,
  `screen_share_on` text DEFAULT NULL,
  `screen_share_off` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tblhr_candidate_meetings`
--
ALTER TABLE `tblhr_candidate_meetings`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tblhr_candidate_meetings`
--
ALTER TABLE `tblhr_candidate_meetings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
desc tblhr_candidate_meetings;


select * from tblhr_candidate_meetings;