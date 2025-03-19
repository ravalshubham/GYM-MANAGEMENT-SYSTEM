-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 28, 2025 at 04:27 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gym`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `admin_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`admin_id`, `name`, `username`, `password`) VALUES
(11, 'Admin One', 'admin1', 'adminpass1'),
(12, 'Admin Two', 'admin2', 'adminpass2');

-- --------------------------------------------------------

--
-- Table structure for table `equipment`
--

CREATE TABLE `equipment` (
  `equipment_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `equipment_type` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `equipment_condition` enum('Good','Needs Repair','Out of Order') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `equipment`
--

INSERT INTO `equipment` (`equipment_id`, `name`, `equipment_type`, `quantity`, `equipment_condition`) VALUES
(1, 'Treadmill', 'Cardio Machine', 5, 'Good'),
(2, 'Dumbbells', 'Strength Training', 20, 'Good'),
(3, 'Bench Press', 'Strength Training', 3, 'Needs Repair'),
(4, 'Rowing Machine', 'Cardio Machine', 2, 'Good'),
(5, 'Leg Press', 'Strength Training', 4, 'Out of Order');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  `rating` int(11) DEFAULT NULL CHECK (`rating` between 1 and 5),
  `feedback_text` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`feedback_id`, `member_id`, `rating`, `feedback_text`) VALUES
(1, 1, 5, 'Great gym environment and helpful trainers!'),
(2, 2, 4, 'Good facilities, but some equipment needs repair.'),
(3, 3, 5, 'Friendly staff and clean environment.'),
(5, 5, 4, 'Membership pricing is fair, but could have more classes.'),
(7, 2, 4, 'this is best gym'),
(8, 3, 4, 'good place');

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `member_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` enum('Male','Female','Other') NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `status` enum('Active','Inactive') DEFAULT 'Active',
  `date_joined` date DEFAULT curdate(),
  `trainer_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`member_id`, `name`, `age`, `gender`, `username`, `password`, `contact_number`, `status`, `date_joined`, `trainer_id`) VALUES
(1, 'John Doe', 25, 'Male', 'john_doe', 'pass123', '1234567890', 'Active', '2025-02-27', NULL),
(2, 'Alice Smith', 30, 'Female', 'alice_smith', '2113', '0987654321', 'Active', '2025-02-27', NULL),
(3, 'Robert Brown', 28, 'Male', 'robert_brown', 'pass789', '1122334455', 'Active', '2025-02-27', NULL),
(4, 'Emily Davis', 22, 'Female', 'emily_davis', 'pass321', '2233445566', 'Active', '2025-02-27', NULL),
(5, 'Michael Wilson', 35, 'Male', 'michael_wilson', 'pass654', '3344556677', 'Active', '2025-02-27', NULL),
(7, 'James Lee', 40, 'Male', 'james_lee', 'pass741', '5566778899', 'Active', '2025-02-27', NULL),
(8, 'Laura White', 29, 'Female', 'laura_white', 'pass852', '6677889900', 'Active', '2025-02-27', NULL),
(9, 'David Clark', 33, 'Male', 'david_clark', 'pass963', '7788990011', 'Active', '2025-02-27', NULL),
(10, 'Sophia Harris', 26, 'Female', 'sophia_harris', 'pass159', '8899001122', 'Active', '2025-02-27', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `memberships`
--

CREATE TABLE `memberships` (
  `membership_id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  `membership_type` varchar(100) NOT NULL,
  `start_date` date NOT NULL,
  `expiry_date` date NOT NULL,
  `price` decimal(10,2) NOT NULL DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `memberships`
--

INSERT INTO `memberships` (`membership_id`, `member_id`, `membership_type`, `start_date`, `expiry_date`, `price`) VALUES
(1, 1, 'Gold', '2023-05-06', '2023-11-06', 0.00),
(2, 2, 'Silver', '2024-02-15', '2025-02-15', 0.00),
(3, 3, 'Gold', '2024-05-06', '2025-09-10', 0.00);

-- --------------------------------------------------------

--
-- Table structure for table `member_workout_plans`
--

CREATE TABLE `member_workout_plans` (
  `member_id` int(11) NOT NULL,
  `workout_plan_id` int(11) NOT NULL,
  `assigned_date` date DEFAULT curdate()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `member_workout_plans`
--

INSERT INTO `member_workout_plans` (`member_id`, `workout_plan_id`, `assigned_date`) VALUES
(1, 1, '2025-02-27'),
(2, 1, '2024-02-05'),
(3, 2, '2025-02-27'),
(4, 5, '2025-02-27');

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `payment_id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `payment_method` enum('Cash','Credit Card','Online') NOT NULL,
  `payment_date` date DEFAULT curdate()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`payment_id`, `member_id`, `amount`, `payment_method`, `payment_date`) VALUES
(1, 1, 500.00, 'Credit Card', '2024-02-01'),
(2, 2, 300.00, 'Cash', '2024-02-05'),
(3, 3, 450.00, 'Online', '2024-02-10'),
(4, 1, 2000.00, 'Cash', '2023-04-05'),
(5, 2, 2000.00, 'Cash', '2023-04-05'),
(6, 3, 2000.00, '', '2020-04-05'),
(7, 1, 3000.00, 'Credit Card', '2024-03-01');

-- --------------------------------------------------------

--
-- Table structure for table `trainers`
--

CREATE TABLE `trainers` (
  `trainer_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `specialization` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `status` enum('Active','Inactive') DEFAULT 'Active',
  `date_joined` date DEFAULT curdate()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `trainers`
--

INSERT INTO `trainers` (`trainer_id`, `name`, `specialization`, `username`, `password`, `contact_number`, `status`, `date_joined`) VALUES
(1, 'Coach Mike', 'Strength Training', 'coach_mike', 'trainer123', '1112223333', 'Active', '2025-02-27'),
(2, 'Lisa Green', 'Yoga & Flexibility', 'lisa_green', 'trainer456', '2223334444', 'Active', '2025-02-27'),
(3, 'Tom Black', 'Cardio & Endurance', 'tom_black', 'trainer789', '3334445555', 'Active', '2025-02-27'),
(4, 'Emma Scott', 'Weight Loss', 'emma_scott', 'trainer321', '4445556666', 'Active', '2025-02-27'),
(5, 'Daniel King', 'Bodybuilding', 'daniel_king', 'trainer654', '5556667777', 'Active', '2025-02-27'),
(16, 'Coach Mike', 'Strength Training', 'coach mike ', 'trainer123', '1112223333', 'Active', '2025-02-27'),
(17, 'Lisa Green', 'Yoga & Flexibility', 'lisa green', 'trainer456', '2223334444', 'Active', '2025-02-27'),
(18, 'Tom Black', 'Cardio & Endurance', 'tom black', 'trainer789', '3334445555', 'Active', '2025-02-27'),
(19, 'Emma Scott', 'Weight Loss', 'emma scott', 'trainer321', '4445556666', 'Active', '2025-02-27'),
(20, 'Daniel King', 'Bodybuilding', 'daniel king', 'trainer654', '5556667777', 'Active', '2025-02-27');

-- --------------------------------------------------------

--
-- Table structure for table `workout_plans`
--

CREATE TABLE `workout_plans` (
  `workout_plan_id` int(11) NOT NULL,
  `workout_plan_name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `duration_weeks` int(11) NOT NULL,
  `difficulty_level` enum('Beginner','Intermediate','Advanced') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `workout_plans`
--

INSERT INTO `workout_plans` (`workout_plan_id`, `workout_plan_name`, `description`, `duration_weeks`, `difficulty_level`) VALUES
(1, 'Beginner Plan', 'A basic plan for new members.', 4, 'Beginner'),
(2, 'Strength Training', 'Focus on muscle gain.', 8, 'Intermediate'),
(3, 'Cardio Burn', 'A plan for endurance and fat loss.', 4, 'Advanced'),
(4, 'Beginner Plan', 'A basic plan for new members.', 4, 'Beginner'),
(5, 'Strength Training', 'Focus on muscle gain.', 8, 'Intermediate'),
(6, 'Cardio Burn', 'A plan for endurance and fat loss.', 6, 'Advanced'),
(7, 'weight loss', 'for loss weight', 5, 'Advanced'),
(8, 'Bulnking', 'gain weight', 3, 'Beginner');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`admin_id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `equipment`
--
ALTER TABLE `equipment`
  ADD PRIMARY KEY (`equipment_id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`feedback_id`),
  ADD KEY `member_id` (`member_id`);

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`member_id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `fk_trainer` (`trainer_id`);

--
-- Indexes for table `memberships`
--
ALTER TABLE `memberships`
  ADD PRIMARY KEY (`membership_id`),
  ADD UNIQUE KEY `unique_member` (`member_id`);

--
-- Indexes for table `member_workout_plans`
--
ALTER TABLE `member_workout_plans`
  ADD PRIMARY KEY (`member_id`,`workout_plan_id`),
  ADD KEY `workout_plan_id` (`workout_plan_id`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`payment_id`),
  ADD KEY `member_id` (`member_id`);

--
-- Indexes for table `trainers`
--
ALTER TABLE `trainers`
  ADD PRIMARY KEY (`trainer_id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `workout_plans`
--
ALTER TABLE `workout_plans`
  ADD PRIMARY KEY (`workout_plan_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admins`
--
ALTER TABLE `admins`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `equipment`
--
ALTER TABLE `equipment`
  MODIFY `equipment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `feedback_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `member_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `memberships`
--
ALTER TABLE `memberships`
  MODIFY `membership_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `trainers`
--
ALTER TABLE `trainers`
  MODIFY `trainer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `workout_plans`
--
ALTER TABLE `workout_plans`
  MODIFY `workout_plan_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `feedback`
--
ALTER TABLE `feedback`
  ADD CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `members` (`member_id`) ON DELETE CASCADE;

--
-- Constraints for table `members`
--
ALTER TABLE `members`
  ADD CONSTRAINT `fk_trainer` FOREIGN KEY (`trainer_id`) REFERENCES `trainers` (`trainer_id`) ON DELETE SET NULL;

--
-- Constraints for table `memberships`
--
ALTER TABLE `memberships`
  ADD CONSTRAINT `fk_membership_member` FOREIGN KEY (`member_id`) REFERENCES `members` (`member_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `memberships_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `members` (`member_id`) ON DELETE CASCADE;

--
-- Constraints for table `member_workout_plans`
--
ALTER TABLE `member_workout_plans`
  ADD CONSTRAINT `fk_workout_member` FOREIGN KEY (`member_id`) REFERENCES `members` (`member_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `member_workout_plans_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `members` (`member_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `member_workout_plans_ibfk_2` FOREIGN KEY (`workout_plan_id`) REFERENCES `workout_plans` (`workout_plan_id`) ON DELETE CASCADE;

--
-- Constraints for table `payments`
--
ALTER TABLE `payments`
  ADD CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `members` (`member_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
