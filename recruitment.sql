-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 03, 2020 at 10:07 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `recruitment`
--

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `name` varchar(20) NOT NULL,
  `location` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`name`, `location`) VALUES
('APIC Pharmaceutical ', 'Nasr City'),
('Arrow Egypt', '5 El-Safa'),
('Canstars Security Se', 'Nasr City'),
('DELL', 'Smart Village 28 Cairo Alexandria desert road, Building 4, S'),
('Delta Pharma', 'Heliopolis'),
('Ebtkarat Information', 'Nasr City'),
('Egypt Pharma', 'Nasr City'),
('ElMnassa Innovation ', 'Alexandria, Egypt'),
('Finicom', 'Alexandria, Egypt'),
('IBM', 'Smart Village Building B144 KM28  Cairo Alex Desert Road'),
('Interface', 'Giza, El Omraniya'),
('Minapharm Pharmaceut', 'Heliopolis'),
('Multipharma', 'Heliopolis'),
('Parkville', 'Cairo'),
('Sanofi Egypt', 'Zeitoun'),
('TAM', 'New Cairo City'),
('Valeo', 'Smart Village 28 Cairo Alexandria desert road'),
('Vanguard Security', 'Zamalek'),
('ZeroTech Egypt', 'Nasr City');

-- --------------------------------------------------------

--
-- Table structure for table `has`
--

CREATE TABLE `has` (
  `c_name` varchar(20) NOT NULL,
  `J_ID` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `has`
--

INSERT INTO `has` (`c_name`, `J_ID`) VALUES
('ElMnassa Innovation ', '000001'),
('ElMnassa Innovation ', '000002'),
('IBM', '000003'),
('TAM', '000004'),
('TAM', '000005');

-- --------------------------------------------------------

--
-- Table structure for table `internselection`
--

CREATE TABLE `internselection` (
  `duration` varchar(7) NOT NULL,
  `ID` varchar(6) NOT NULL,
  `InternshipTitle` varchar(100) NOT NULL,
  `Payment` varchar(6) NOT NULL,
  `Field` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `internselection`
--

INSERT INTO `internselection` (`duration`, `ID`, `InternshipTitle`, `Payment`, `Field`) VALUES
('6 weeks', '000008', 'Android Developer', 'paid', 'android application devel'),
('6 weeks', '000008', 'Android Developer', 'paid', 'android application devel');

-- --------------------------------------------------------

--
-- Table structure for table `internship`
--

CREATE TABLE `internship` (
  `duration` varchar(7) NOT NULL,
  `ID` varchar(6) NOT NULL,
  `InternshipTitle` varchar(100) NOT NULL,
  `Payment` varchar(6) NOT NULL,
  `Field` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `internship`
--

INSERT INTO `internship` (`duration`, `ID`, `InternshipTitle`, `Payment`, `Field`) VALUES
('1 month', '000001', 'Cloud Developer ', 'unpaid', 'cloud development'),
('1 month', '000002', 'Software Engineer', 'unpaid', 'software engineering'),
('2 month', '000003', 'Internal Communication ', 'unpaid', 'Internal Communication'),
('1 month', '000004', 'Graphic designer', 'unpaid', 'Graphic design'),
('3 month', '000005', 'Web Developer', 'unpaid', 'Web development'),
('6 weeks', '000006', 'Mobile App Tester', 'paid', 'Mobile Application testin'),
('6 weeks', '000007', 'iOS Developer', 'paid', 'iOS application developer'),
('6 weeks', '000008', 'Android Developer', 'paid', 'android application devel'),
('1 month', '000009', 'Medical Representitive', 'paid', 'Pharmacy');

-- --------------------------------------------------------

--
-- Table structure for table `job`
--

CREATE TABLE `job` (
  `salary` varchar(20) NOT NULL,
  `J_ID` varchar(6) NOT NULL,
  `experience` int(8) NOT NULL,
  `skills` varchar(250) NOT NULL,
  `title` varchar(35) NOT NULL,
  `field` varchar(30) NOT NULL,
  `Type` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `job`
--

INSERT INTO `job` (`salary`, `J_ID`, `experience`, `skills`, `title`, `field`, `Type`) VALUES
('Confidential', '000001', 2, 'BS/MS degree in Computer Science, Engineering or a related subject,\r\nHave published 5 or more iOS apps in the app store, Proficient understanding of code versioning tools,\r\nWorking knowledge of the general mobile landscape, architectures, and trends', 'iOS Developer', 'iOS application development', 'full-time'),
('Confidential', '000002', 2, 'BS/MS degree in Computer Science, Proven software development experience and Android skills development,\r\nProven working experience in Android app development for more than 1 professional year,\r\nHave published at least Five original Android app,\r\n', 'Android Developer', 'Android application developmen', 'full-time'),
('Confidential', '000003', 1, 'worked with cloud based application ,experince in troubleshooting network commpunication issues , excellent comenication skills , can work proactively and efficiently', 'Cloud Infrastructure', 'Cloud development', 'full-time'),
('Confidential', '000004', 3, 'Strong knowledge of software QA methodologies, tools and processes.\r\nExperience in writing test plans is a plus.\r\nExperience in writing test scenarios and test cases.\r\nExperience in handling Load, stress and performance testing.\r\n', 'Senior Software Tester', 'Software Testing', 'full-time'),
('Confidential', '000005', 2, 'Strong knowledge of OOP programming, Strong DB skills, Experince in .NRT framework and . NET Core', 'Senior Full-Stack Developer', 'Software development', 'full-time');

-- --------------------------------------------------------

--
-- Table structure for table `jobselection`
--

CREATE TABLE `jobselection` (
  `Salary` varchar(20) NOT NULL,
  `J_ID` varchar(6) NOT NULL,
  `experience` int(11) NOT NULL,
  `skills` varchar(250) NOT NULL,
  `title` varchar(35) NOT NULL,
  `Field` varchar(30) NOT NULL,
  `Type` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `offer`
--

CREATE TABLE `offer` (
  `cname` varchar(20) NOT NULL,
  `intern_ID` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `offer`
--

INSERT INTO `offer` (`cname`, `intern_ID`) VALUES
('Dell', '000003'),
('Dell', '000004'),
('ElMnassa Innovation ', '000006'),
('ElMnassa Innovation ', '000007'),
('ElMnassa Innovation ', '000008'),
('Finicom', '000005'),
('IBM', '000001'),
('Interface', '000002'),
('Parkville', '000009');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `has`
--
ALTER TABLE `has`
  ADD PRIMARY KEY (`c_name`,`J_ID`),
  ADD KEY `J_ID` (`J_ID`);

--
-- Indexes for table `internship`
--
ALTER TABLE `internship`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `job`
--
ALTER TABLE `job`
  ADD PRIMARY KEY (`J_ID`);

--
-- Indexes for table `offer`
--
ALTER TABLE `offer`
  ADD PRIMARY KEY (`cname`,`intern_ID`),
  ADD KEY `intern_ID` (`intern_ID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `has`
--
ALTER TABLE `has`
  ADD CONSTRAINT `has_ibfk_1` FOREIGN KEY (`c_name`) REFERENCES `company` (`name`) ON UPDATE CASCADE,
  ADD CONSTRAINT `has_ibfk_2` FOREIGN KEY (`J_ID`) REFERENCES `job` (`J_ID`) ON UPDATE CASCADE;

--
-- Constraints for table `offer`
--
ALTER TABLE `offer`
  ADD CONSTRAINT `offer_ibfk_1` FOREIGN KEY (`cname`) REFERENCES `company` (`name`) ON UPDATE CASCADE,
  ADD CONSTRAINT `offer_ibfk_2` FOREIGN KEY (`intern_ID`) REFERENCES `internship` (`ID`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
