-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 02, 2020 at 06:05 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flaskproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(6) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `img` varchar(20) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `img`, `date`) VALUES
(1, 'Internet', 'this is my first post', 'page1', 'hello brothrer internate is not working', 'about-bg.jpg', '2020-09-29 21:38:06'),
(2, 'python code', 'hello my second post', 'page2', 'Checkboxes and radios use are built to support HTML', 'about-bg.jpg', '2020-10-02 17:35:14'),
(3, 'jinu', 'hdbsfk', 'hdbvs', 'skhdb .kjcvs', 'about-bg.jpg', '2020-10-02 17:14:16'),
(5, 'sugdbi;vs', 'yfguhlij;l', 'yguhlj;kl;', 'guhi;jok;l,', 'ykuhlnjklk,', '2020-10-02 20:22:03'),
(6, 'yglhkjl', 'ygubhlinjkl', 'iygubhinjk', 'yvgubhijl', 'e5urt7iyohuijoik', '2020-10-02 20:22:18'),
(7, 'yfgkubhlnj;lmk', 'ivygubhnijmlk', 'iygbuhlnj;mkl', 'ygubhinjlk', '68t7iyuijo', '2020-10-02 20:22:32'),
(8, 'utyvbuhinjomk', 'fygubhnjmlk', 'fygkjhlk', 'yubhnijm', 'uygbuhnij', '2020-10-02 20:22:42'),
(9, 'ufyvgkubhlinj', 'ygbuhlnj', 'guhnjmlk', 'gbuhnijm', 'yvgbukhlnij', '2020-10-02 20:22:54');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
