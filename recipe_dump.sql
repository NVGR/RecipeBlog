-- MySQL dump 10.13  Distrib 5.6.32, for osx10.11 (x86_64)
--
-- Host: localhost    Database: recipedb
-- ------------------------------------------------------
-- Server version	5.6.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `recipe_recipes`
--

DROP TABLE IF EXISTS `recipe_recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipe_recipes` (
  `recipe_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `owner` varchar(50) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`recipe_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe_recipes`
--

LOCK TABLES `recipe_recipes` WRITE;
/*!40000 ALTER TABLE `recipe_recipes` DISABLE KEYS */;
INSERT INTO `recipe_recipes` VALUES (2,'Chicken Biryani','Awesome Chicken Biryani!!!','admin','2016-10-26 12:34:02.977532','2016-10-26 12:34:02.977571'),(3,'Mutton Biryani','Awesome Mutton Biryani!!','admin','2016-10-26 12:34:36.704698','2016-10-26 12:34:36.704745'),(4,'Shrimp Biryani','Awesome Shrimp Biryani!!! Awesome Shrimp Biryani!!! Awesome Shrimp Biryani!!! Awesome Shrimp Biryani!!! Awesome Shrimp Biryani!!! Awesome Shrimp Biryani!!! Awesome Shrimp Biryani!!! Awesome Shrimp Biryani!!! Awesome Shrimp Biryani!!! Awesome Shrimp Biryani!!! Awesome Shrimp Biryani!!! Awesome Shrimp Biryani!!! Awesome Shrimp Biryani!!! Awesome Shrimp Biryani!!!','admin','2016-10-26 20:01:16.393566','2016-10-26 12:35:31.254688'),(5,'Veg Biryani','Awesome Veg Biryani!!','Venugopal','2016-10-26 12:38:34.204606','2016-10-26 12:38:34.204646'),(6,'Egg Curry','Delicious Egg Curry!!','Venugopal','2016-10-26 12:39:02.056184','2016-10-26 12:39:02.056225'),(7,'Kesari','Superb Kesari!!','Venugopal','2016-10-26 12:39:28.898180','2016-10-26 12:39:28.898216'),(8,'Chicken 65','Superb Chicken 65!!!','Venugopal','2016-10-26 12:39:52.403852','2016-10-26 12:39:52.403918');
/*!40000 ALTER TABLE `recipe_recipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe_steps`
--

DROP TABLE IF EXISTS `recipe_steps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipe_steps` (
  `step_id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `owner` varchar(50) NOT NULL,
  `recipe_id` int(11) NOT NULL,
  PRIMARY KEY (`step_id`),
  KEY `recipe_steps_recipe_id_50079289_fk_recipe_recipes_recipe_id` (`recipe_id`),
  CONSTRAINT `recipe_steps_recipe_id_50079289_fk_recipe_recipes_recipe_id` FOREIGN KEY (`recipe_id`) REFERENCES `recipe_recipes` (`recipe_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe_steps`
--

LOCK TABLES `recipe_steps` WRITE;
/*!40000 ALTER TABLE `recipe_steps` DISABLE KEYS */;
INSERT INTO `recipe_steps` VALUES (4,1,'Step 1','admin',4),(5,2,'Step 2','admin',4),(6,4,'Step 4','admin',4),(7,3,'Step 3','admin',4),(8,5,'Step 5','admin',4),(10,1,'step 1','admin',3);
/*!40000 ALTER TABLE `recipe_steps` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-10-27  0:51:52
