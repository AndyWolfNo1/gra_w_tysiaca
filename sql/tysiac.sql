-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 19 Maj 2020, 13:01
-- Wersja serwera: 10.4.8-MariaDB
-- Wersja PHP: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `tysiac`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `gracze`
--

CREATE TABLE `gracze` (
  `ID` int(11) NOT NULL,
  `login` text COLLATE utf8mb4_polish_ci NOT NULL,
  `passwd` text COLLATE utf8mb4_polish_ci NOT NULL,
  `name` text COLLATE utf8mb4_polish_ci NOT NULL,
  `points` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;

--
-- Zrzut danych tabeli `gracze`
--

INSERT INTO `gracze` (`ID`, `login`, `passwd`, `name`, `points`) VALUES
(1, 'Lasza', 'd4cb0ebeee4fa1c62e27898818eeaa9f', 'Marcin', 0),
(2, 'Buczo', 'd2e5ff6d027b9f674391b2a402adb363', 'Tomek', 0),
(3, 'Polmos', 'd09f49dc98df20ae259d6ecd8a61c4f8', 'Tomek', 0),
(4, 'Sebix', 'd3e62c6c5e96bdee6f23fdcaa2505527', 'Sebastnian', 0),
(5, 'Prezes', '5a1a31b0ae38f1e6ed3157931e5609cb', 'pioter', 0);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `tables`
--

CREATE TABLE `tables` (
  `ID` int(11) NOT NULL,
  `author` text COLLATE utf8mb4_polish_ci NOT NULL,
  `stan` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;

--
-- Zrzut danych tabeli `tables`
--

INSERT INTO `tables` (`ID`, `author`, `stan`) VALUES
(1, 'Lasza', 0),
(11, 'Buczo', 0),
(12, 'Lasza', 0),
(13, 'Polmos', 0),
(14, 'Sebix', 0),
(15, 'Sebix', 0),
(16, 'Prezes', 0);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `t_p`
--

CREATE TABLE `t_p` (
  `ID` int(11) NOT NULL,
  `name` text COLLATE utf8mb4_polish_ci NOT NULL,
  `chair` int(11) NOT NULL,
  `table_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;

--
-- Zrzut danych tabeli `t_p`
--

INSERT INTO `t_p` (`ID`, `name`, `chair`, `table_ID`) VALUES
(1, 'buczo', 2, 11),
(2, 'lasza', 1, 11),
(3, 'lasza', 1, 1),
(4, 'polmos', 4, 11),
(5, 'sebix', 3, 11),
(6, 'sebix', 4, 1);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `gracze`
--
ALTER TABLE `gracze`
  ADD PRIMARY KEY (`ID`);

--
-- Indeksy dla tabeli `tables`
--
ALTER TABLE `tables`
  ADD PRIMARY KEY (`ID`);

--
-- Indeksy dla tabeli `t_p`
--
ALTER TABLE `t_p`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `gracze`
--
ALTER TABLE `gracze`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT dla tabeli `tables`
--
ALTER TABLE `tables`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT dla tabeli `t_p`
--
ALTER TABLE `t_p`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
