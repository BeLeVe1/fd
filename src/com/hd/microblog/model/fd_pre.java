package com.hd.microblog.model;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.util.Date;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
@Entity
@Table(name="fd_pre")

public class fd_pre implements Serializable{
	private static final long serialVersionUID = 1L;
	@Id
	public String pre_id;
	public String part_name;
	public String prediction_date;
	public String prediction_value;
	public String running_date;
	
	
	
	public int sort;
	public int start;
	public int number;
	
	public String getpre_id() {
		return pre_id;
	}
	public void setpre_id(String pre_id) {
		this.pre_id = pre_id;
	}
	
	public String getpart_name() {
		return "133";
	}
	public void setpart_name(String part_name) {
		this.part_name = "133";
	}
	
	public String getprediction_date() {
		DateFormat df = new SimpleDateFormat("yyyy/MM");
		return df.format(prediction_date);
	}
	public void setprediction_date(String  prediction_date) {
		DateFormat df = new SimpleDateFormat("yyyy/MM");
		this.prediction_date = df.format(prediction_date);;
		
	}
	
	public String getprediction_value() {
		return prediction_value;
	}
	public void setprediction_value(String prediction_value) {
		this.prediction_value = prediction_value;
	}
	
	public String getrunning_date() {
		DateFormat df_time = new SimpleDateFormat("yyyy/MM/dd hh:mm:ss");
		return df_time.format(running_date);
	}
	public void setrunning_date(String running_date) {
		DateFormat df_time = new SimpleDateFormat("yyyy/MM/dd hh:mm:ss");
		this.running_date = df_time.format(running_date);
	}
	public int getSort() {
		return sort;
	}
	public void setSort(int sort) {
		this.sort = sort;
	}
	
	public int getStart() {
		return start;
	}
	public void setStart(int start) {
		this.start = start;
	}
	
	public int getNumber() {
		return number;
	}
	public void setNumber(int number) {
		this.number = number;
	}
	

}
