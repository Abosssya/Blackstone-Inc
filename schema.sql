CREATE DATABASE IF NOT EXISTS Blackstone_ERP;
USE Blackstone_ERP;

CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Role VARCHAR(50),
    Office_Location VARCHAR(50)
);

CREATE TABLE Companies (
    CompanyID INT AUTO_INCREMENT PRIMARY KEY,
    Ticker VARCHAR(10) NOT NULL UNIQUE,
    Sector VARCHAR(50),
    Industry VARCHAR(50)
);

CREATE TABLE Financials (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,
    CompanyId INT,
    EBITDA DECIMAL(18, 2),
    Net_Income DECIMAL(18, 2),
    Fiscal_Year INT,
    CONSTRAINT fk_financials_company FOREIGN KEY (CompanyId) 
        REFERENCES Companies(CompanyID) ON DELETE CASCADE
);

CREATE TABLE Valuations (
    ModelID INT AUTO_INCREMENT PRIMARY KEY,
    CompanyId INT,
    AnalystId INT,
    WACC DECIMAL(5, 4), -- Stored as decimal (e.g. 0.0850)
    Multiple DECIMAL(5, 2),
    CONSTRAINT fk_valuations_company FOREIGN KEY (CompanyId) 
        REFERENCES Companies(CompanyID) ON DELETE CASCADE,
    CONSTRAINT fk_valuations_user FOREIGN KEY (AnalystId) 
        REFERENCES Users(UserID) ON DELETE SET NULL
);

INSERT INTO Users (Name, Role, Office_Location) VALUES 
('Ayden Shaw', 'Senior Analyst', 'New York'),
('Mason Mount', 'Managing Director', 'London');

INSERT INTO Companies (Ticker, Sector, Industry) VALUES 
('HLT', 'Consumer Cyclical', 'Hotels & Resorts'),
('CQP', 'Energy', 'Oil & Gas Midstream');

INSERT INTO Financials (CompanyId, EBITDA, Net_Income, Fiscal_Year) VALUES 
(1, 2880000000.00, 1457000000.00, 2026), 
(2, 4428000000.00, 2987000000.00, 2026);   

INSERT INTO Valuations (CompanyId, AnalystId, WACC, Multiple) VALUES 
(1, 1, 0.0750, 9.50), 
(2, 2, 0.0950, 14.50); 
