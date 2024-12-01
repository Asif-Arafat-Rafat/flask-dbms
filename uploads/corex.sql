-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 23, 2024 at 08:41 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `corex`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `username`, `password`) VALUES
(1, 'rafat', '@sif');

-- --------------------------------------------------------

--
-- Table structure for table `carousel`
--

CREATE TABLE `carousel` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `front_image` text NOT NULL,
  `left_image` text NOT NULL,
  `right_image` text NOT NULL,
  `title` text NOT NULL,
  `sub_title` text NOT NULL,
  `extra_info` text NOT NULL,
  `added` date NOT NULL,
  `position` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- Dumping data for table `carousel`


INSERT INTO `carousel` (`id`, `name`, `front_image`, `left_image`, `right_image`, `title`, `sub_title`, `extra_info`, `added`, `position`) VALUES
(1, 'Router', 'front.png', 'left.png', 'right.png', 'Stay Connected, Study Better', 'Strong signal, strong results.', 'Uninterrupted learning and fun, all day long', '2024-09-23', 1),
(3, 'Fan', 'fan_front.png', 'fan_left.png', 'fan_right.png', 'Stay Cool, Stay Focused', 'Quiet comfort for your study sessions', 'Beat the heat and stay productive', '2024-09-23', 2),
(4, 'Bulb', 'bulb.png', 'bulb-left.png', 'bulb-right.png', 'bulb', 'light', 'bright', '2024-09-23', 2);

--------------------------------------------------------


-- Table structure for table `cart`


CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `per_price` float NOT NULL,
  `total_price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `order_date` datetime DEFAULT current_timestamp(),
  `status` tinyint(1) NOT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  `payment_method` varchar(50) DEFAULT NULL,
  `delivery_address` text DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `delivery_time` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `Employees` (
    -- Basic Attributes
    employee_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier with auto-increment
    first_name VARCHAR(50) NOT NULL,             -- Required field for the employee's first name
    last_name VARCHAR(50) NOT NULL,              -- Required field for the employee's last name
    
    -- Unique and Default Constraints
    email VARCHAR(100) UNIQUE,                   -- Email must be unique
    hire_date DATE DEFAULT CURRENT_DATE,         -- Default to current date if no value is provided
    
    -- Numeric and Decimal Types
    salary DECIMAL(10, 2) CHECK (salary >= 0),   -- Salary must be non-negative
    
    -- Enum and Boolean
    job_title ENUM('Manager', 'Developer', 'Analyst', 'Intern') DEFAULT 'Intern', -- Specific set of values
    is_active BOOLEAN DEFAULT TRUE,             -- Boolean value with a default
    
    -- Foreign Key Example
    department_id INT,                           -- Reference to the department
    FOREIGN KEY (department_id) REFERENCES Departments(department_id) ON DELETE SET NULL,
    
    -- Index for Faster Search
    -- INDEX (last_name),
    
    -- Timestamp Attributes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Automatically set when a row is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Updated on row modification
);


--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_id`, `user_id`, `order_date`, `status`, `total_price`, `payment_method`, `delivery_address`, `phone_number`, `delivery_time`) VALUES
(2, 1, '2024-10-20 15:23:03', 1, 8.00, NULL, 'kuet', '017278356', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `order_items`
--

CREATE TABLE `order_items` (
  `order_item_id` int(11) NOT NULL,
  `order_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `price_per_item` decimal(10,2) DEFAULT NULL,
  `total_price` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_items`
--

INSERT INTO `order_items` (`order_item_id`, `order_id`, `product_id`, `quantity`, `price_per_item`, `total_price`) VALUES
(1, 2, 1, 4, 2.00, 8.00);

-- --------------------------------------------------------

--
-- Table structure for table `pc_repair`
--

CREATE TABLE `pc repair` (
  `query_id` int(11) NOT NULL,
  `phone_number` text NOT NULL,
  `urgency` text DEFAULT NULL,
  `components` text DEFAULT NULL,
  `details` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pc_repair`
--

INSERT INTO `pc repair` (`query_id`, `phone_number`, `urgency`, `components`, `details`) VALUES
(1, '01839497606', '24', 'Desktop', 'hello'),
(2, '01839497606', '12', 'Desktop', 'testing');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `name` text NOT NULL,
  `image` text NOT NULL,
  `category` text NOT NULL,
  `brand` text NOT NULL,
  `description` text NOT NULL,
  `stock` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `b_price` int(11) NOT NULL,
  `discount` int(11) DEFAULT NULL,
  `sold` int(11) DEFAULT NULL,
  `voted` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `varients` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `name`, `image`, `category`, `brand`, `description`, `stock`, `price`, `b_price`, `discount`, `sold`, `voted`, `score`, `varients`) VALUES
(1, 't1', 'keyboard1.png', 'Keyboard', 'Unknown', 'sme', 2, 2, 1, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--
CREATE TABLE `Users` (
    id1 INT AUTO_INCREMENT PRIMARY KEY,        
    username VARCHAR(50) NOT NULL UNIQUE,     
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `f_name` text NOT NULL,
  `l_name` text DEFAULT NULL,
  `phone` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `address` text DEFAULT NULL,
  `Date of birth` int DEFAULT NULL,
  `joined` date DEFAULT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `f_name`, `l_name`, `phone`, `email`, `address`, `date of birth`, `joined`, `password`) VALUES
(1, 's', NULL, NULL, 's', NULL, NULL, NULL, '$2y$10$A.FoPZ74JAmZfJXlPm29KuA2qPFff2qjCOwLbsV87LqBiA4nrbwZC');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `carousel`
--
ALTER TABLE `carousel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`cart_id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `order_items`
--
ALTER TABLE `order_items`
  ADD PRIMARY KEY (`order_item_id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `pc_repair`
--
ALTER TABLE `pc_repair`
  ADD PRIMARY KEY (`query_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `phone` (`phone`) USING HASH,
  ADD UNIQUE KEY `email` (`email`) USING HASH;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `carousel`
--
ALTER TABLE `carousel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `cart_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `order_items`
--
ALTER TABLE `order_items`
  MODIFY `order_item_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `pc_repair`
--
ALTER TABLE `pc_repair`
  MODIFY `query_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `order_items`
--
ALTER TABLE `order_items`
  ADD CONSTRAINT `order_items_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`),
  ADD CONSTRAINT `order_items_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
