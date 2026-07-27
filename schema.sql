
CREATE DATABASE IF NOT EXISTS news_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE news_db;


CREATE TABLE IF NOT EXISTS headlines(
  id INT AUTO_INCREMENT PRIMARY KEY,
  fetch_date DATE NOT NULL,
  headline VARCHAR(500) NOT NULL,
  url_link VARCHAR(1000) NOT NULL,

  UNIQUE KEY unique_story(fetch_date, headline(255))



) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
