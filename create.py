-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`usuario` (
  `user` VARCHAR(20) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  `sistema_id` INT NOT NULL,
  PRIMARY KEY (`user`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`postagem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`postagem` (
  `idpostagem` INT NOT NULL,
  `data` DATETIME NOT NULL,
  `usuario_user` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`idpostagem`),
  INDEX `fk_postagem_usuario1_idx` (`usuario_user` ASC) VISIBLE,
  CONSTRAINT `fk_postagem_usuario1`
    FOREIGN KEY (`usuario_user`)
    REFERENCES `mydb`.`usuario` (`user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`mensagem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`mensagem` (
  `idmensagem` INT NOT NULL,
  `mensagem` VARCHAR(100) NOT NULL,
  `data` DATETIME NOT NULL,
  `likes` INT NOT NULL,
  `usuario_user` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`idmensagem`),
  INDEX `fk_mensagem_usuario_idx` (`usuario_user` ASC) VISIBLE,
  CONSTRAINT `fk_mensagem_usuario`
    FOREIGN KEY (`usuario_user`)
    REFERENCES `mydb`.`usuario` (`user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;