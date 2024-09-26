-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema projeto
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema projeto
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `projeto` DEFAULT CHARACTER SET utf8 ;
USE `projeto` ;

-- -----------------------------------------------------
-- Table `projeto`.`modelos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto`.`modelos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `modelo` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projeto`.`fabricantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto`.`fabricantes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_modelo` INT NOT NULL,
  `fabricante` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_fabricantes_modelos1_idx` (`id_modelo` ASC) VISIBLE,
  CONSTRAINT `fk_fabricantes_modelos1`
    FOREIGN KEY (`id_modelo`)
    REFERENCES `projeto`.`modelos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projeto`.`cores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto`.`cores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projeto`.`carros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto`.`carros` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_fabricante` INT NOT NULL,
  `id_cor` INT NOT NULL,
  `placa` VARCHAR(10) NOT NULL,
  `data_cadastro` DATE NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_carros_fabricantes_idx` (`id_fabricante` ASC) VISIBLE,
  INDEX `fk_carros_cores1_idx` (`id_cor` ASC) VISIBLE,
  CONSTRAINT `fk_carros_fabricantes`
    FOREIGN KEY (`id_fabricante`)
    REFERENCES `projeto`.`fabricantes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_carros_cores1`
    FOREIGN KEY (`id_cor`)
    REFERENCES `projeto`.`cores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
