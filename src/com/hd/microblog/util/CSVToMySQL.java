package com.hd.microblog.util;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.opencsv.CSVReader;

import java.io.BufferedReader;
import java.io.FileReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import com.opencsv.CSVReader;

public class CSVToMySQL {
	
	public static String save()  {
      String jdbcURL = "jdbc:mysql://localhost/bd_sys?useUnicode=true&characterEncoding=utf-8";
      String username = "root";
      String password = "123456";
      String csvFilePath = "D:\\train.csv";

      try {
         Connection connection = DriverManager.getConnection(jdbcURL, username, password);
         String[] nextLine;
         String cvsSplitBy = ",";
         String sql = "INSERT INTO fd_pre(part_name, prediction_value) VALUES (?, ?)";
         PreparedStatement statement = connection.prepareStatement(sql);

         BufferedReader reader = new BufferedReader(new FileReader(csvFilePath));
         CSVReader csvReader = new CSVReader(reader);
        while ((nextLine = csvReader.readNext()) != null){
        	String joinedString = String.join(",", nextLine);
            String[] data = joinedString.split(cvsSplitBy);
            statement.setString(1, "IGBT");
            statement.setString(2, data[1]);
            
            statement.executeUpdate();
         }
         csvReader.close();
         reader.close();
         statement.close();
         connection.close();
         return "csvsuccess";
        
      } catch (SQLException e) {
         System.out.println("Connection failed: " + e.getMessage());
         return "csvfail";
      } catch (Exception e) {
         System.out.println("Error reading CSV file: " + e.getMessage());
         return "csvfail";
      }
      
   }
}



