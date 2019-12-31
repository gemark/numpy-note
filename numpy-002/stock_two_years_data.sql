/*
 Navicat Premium Data Transfer

 Source Server         : 本机数据库5.7.26
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : bilibili

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 31/12/2019 17:13:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for stock_two_years_data
-- ----------------------------
DROP TABLE IF EXISTS `stock_two_years_data`;
CREATE TABLE `stock_two_years_data`  (
  `update` date NULL DEFAULT NULL,
  `num` bigint(20) UNSIGNED NULL DEFAULT NULL,
  `stock_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `rise` double NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
