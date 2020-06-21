-- MySQL dump 10.13  Distrib 5.1.53, for Win64 (unknown)
--
-- Host: localhost    Database: pencore
-- ------------------------------------------------------
-- Server version	5.1.53-community-log

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
-- Table structure for table `carmodels`
--

DROP TABLE IF EXISTS `carmodels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `carmodels` (
  `modelid` varchar(45) NOT NULL DEFAULT '',
  `modelName` varchar(45) NOT NULL DEFAULT '',
  `price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`modelName`,`modelid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carmodels`
--

LOCK TABLES `carmodels` WRITE;
/*!40000 ALTER TABLE `carmodels` DISABLE KEYS */;
INSERT INTO `carmodels` VALUES ('102','A3','8900000.00'),('106','A6','9600000.00'),('101','Q3','5600000.00'),('103','Q5','7800000.00'),('104','Q8','8500000.00'),('105','S5','9500000.00');
/*!40000 ALTER TABLE `carmodels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carsale`
--

DROP TABLE IF EXISTS `carsale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `carsale` (
  `prospId` int(11) DEFAULT NULL,
  `regid` varchar(20) NOT NULL DEFAULT '',
  `saledate` date DEFAULT NULL,
  `modelid` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`regid`),
  KEY `prospId` (`prospId`),
  KEY `modelid` (`modelid`),
  CONSTRAINT `carsale_ibfk_1` FOREIGN KEY (`prospId`) REFERENCES `prospect` (`prospId`),
  CONSTRAINT `carsale_ibfk_2` FOREIGN KEY (`modelid`) REFERENCES `carmodels` (`modelName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carsale`
--

LOCK TABLES `carsale` WRITE;
/*!40000 ALTER TABLE `carsale` DISABLE KEYS */;
INSERT INTO `carsale` VALUES (2,'201','2019-12-12',NULL),(3,'202','2020-04-30',NULL),(4,'203','2020-02-20',NULL),(2,'s101','2019-12-12','Q3'),(3,'s102','2020-04-20','A3'),(4,'s103','2020-02-02','Q3'),(5,'s104','2016-02-12','Q5'),(6,'s105','2017-02-02','Q5'),(7,'s106','2018-02-02','Q5'),(8,'s107','2018-02-02','Q5'),(9,'s108','2019-02-02','Q5'),(10,'s109','2020-05-14','Q5'),(11,'s110','2016-06-08','Q3'),(12,'s111','2017-06-08','Q3'),(13,'s112','2017-06-08','Q3'),(14,'s113','2019-06-08','Q3'),(15,'s114','2020-06-08','Q3'),(16,'s115','2016-06-08','A3'),(17,'s116','2016-05-28','A3'),(18,'s117','2018-05-28','A3'),(19,'s118','2019-12-08','A3'),(20,'s119','2019-12-24','A3'),(21,'s120','2020-12-12','A3'),(22,'s121','2016-05-14','S5'),(23,'s122','2018-05-14','S5'),(24,'s123','2019-06-14','S5'),(25,'s124','2020-01-14','S5'),(26,'s125','2017-08-25','Q8'),(27,'s126','2017-08-25','Q8'),(28,'s127','2019-08-25','Q8'),(29,'s128','2020-06-06','A6'),(30,'s129','2020-05-05','A6'),(31,'s130','2020-06-06','A6'),(32,'s131','2016-05-05','A6');
/*!40000 ALTER TABLE `carsale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `userName` varchar(45) NOT NULL,
  `userPass` varchar(20) DEFAULT NULL,
  `userType` varchar(10) DEFAULT NULL,
  `fullName` varchar(50) DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `status` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('D001','password1','admin','devesh','m','8957770436','devesh@gmail.com','activated'),('deepu','password','monitor','deepu','m','7418529630','awas vikas 3 kanpur','activated'),('E001','password1','admin','kuldeep','m','8512099003','kuldeep@gmail.com','activated'),('james','pass','monitor','jameskumar','m','4568521973','james@gmail.com','activated');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prospect`
--

DROP TABLE IF EXISTS `prospect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prospect` (
  `prospId` int(11) NOT NULL AUTO_INCREMENT,
  `prospName` varchar(45) DEFAULT NULL,
  `prospPhone` varchar(45) DEFAULT NULL,
  `prospAddress` varchar(45) DEFAULT NULL,
  `modelName` varchar(45) DEFAULT NULL,
  `interestedColor` varchar(45) DEFAULT NULL,
  `dateOfVisit` varchar(20) DEFAULT NULL,
  `dayOfVisit` varchar(10) DEFAULT NULL,
  `bookingAmount` decimal(12,2) DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  `incomeGroup` varchar(1) DEFAULT NULL,
  `priority` varchar(45) DEFAULT NULL,
  `purchaseMode` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`prospId`),
  KEY `modelName` (`modelName`),
  CONSTRAINT `prospect_ibfk_1` FOREIGN KEY (`modelName`) REFERENCES `carmodels` (`modelName`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prospect`
--

LOCK TABLES `prospect` WRITE;
/*!40000 ALTER TABLE `prospect` DISABLE KEYS */;
INSERT INTO `prospect` VALUES (2,'james','8529634100','LA','Q3','black','2019-12-12','monday','300000.00','n','m','high','creditcard'),(3,'neena','7415296301','california','A3','red','2020-04-20','wednesday','999999.99','f','m','medium','cash'),(4,'smith','6549873210','india','Q3','mattblack','2020-02-02','friday','5000000.00','m','m','low','cash'),(5,'kimberlee','7896547896','America','Q5','white','2016-02-12','monday','500000.00','m','m','medium','cash'),(6,'john','9896547896','America','Q5','white','2017-02-12','monday','600000.00','m','m','medium','cash'),(7,'jimmy','8966547896','UK','Q5','white','2018-02-12','monday','600000.00','m','m','medium','cash'),(8,'jay','2166547896','UK','Q5','white','2018-02-12','monday','600000.00','m','m','medium','cash'),(9,'may','2166540006','Australia','Q5','white','2019-02-12','tuesday','800000.00','m','m','low','creditcard'),(10,'brock','9632540006','India','Q5','black','2020-05-14','thursday','800000.00','m','h','high','creditcard'),(11,'norman','1632540006','Germany','Q3','black','2016-06-08','sunday','800000.00','m','h','high','creditcard'),(12,'natsha','1252540006','Germany','Q3','black','2017-06-08','sunday','800000.00','f','h','high','creditcard'),(13,'maria','1892540006','America','Q3','black','2017-06-08','monday','850000.00','f','h','high','creditcard'),(14,'shuriti','9412611674','California','Q3','red','2019-06-08','monday','850000.00','f','h','high','creditcard'),(15,'devesh','9412611674','India','Q3','mattblack','2020-06-08','wednesday','850000.00','m','h','low','creditcard'),(16,'kshitij','9412685474','India','A3','mattblack','2016-06-08','wednesday','780000.00','m','h','low','creditcard'),(17,'richa','9412685474','India','A3','red','2016-05-28','monday','580000.00','f','h','high','creditcard'),(18,'riya','641585474','India','A3','red','2018-05-28','thurday','980000.00','f','h','high','creditcard'),(19,'natalia','3251585474','Atlanta','A3','grey','2019-12-08','thurday','980000.00','f','h','high','creditcard'),(20,'braun','9251585474','Austria','A3','grey','2019-12-24','thurday','90000.00','m','m','high','creditcard'),(21,'shammi','4551585474','Australia','A3','black','2020-12-24','sunday','490000.00','m','m','low','creditcard'),(22,'mrx','3451585474','Antartica','S5','black','2016-05-14','monday','900000.00','f','h','high','cash'),(23,'kristen','8551585474','England','S5','grey','2018-05-14','monday','980000.00','m','h','high','cash'),(24,'jackson','8351585474','England','S5','mattred','2019-06-14','saturday','680000.00','m','h','high','cash'),(25,'simran','9851585474','Nagaland','S5','red','2020-01-14','saturday','680000.00','f','h','high','cheque'),(26,'hamby','2351585474','Lasvegas','Q8','grey','2017-08-25','monday','680000.00','m','h','high','cheque'),(27,'obama','9521585474','LA','Q8','black','2017-08-25','monday','680000.00','m','h','low','cheque'),(28,'Anne','8521585474','London','Q8','black','2019-08-25','saturday','950000.00','f','h','high','cheque'),(29,'trump','7854123690','America','A6','red','2020-06-06','monday','650000.00','m','m','high','cash'),(30,'misty','7896523140','Kanpur','A6','black','2020-05-05','wednesday','850000.00','f','m','medium','card'),(31,'garvesh','1236547890','Kanpur17','A6','black','2020-06-06','wednesday','800000.00','m','m','high','creditcard'),(32,'mark','7412589630','Simivalley','A6','red','2016-05-05','sunday','700000.00','m','m','low','cash');
/*!40000 ALTER TABLE `prospect` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-20 18:10:02
