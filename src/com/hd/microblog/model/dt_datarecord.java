package com.hd.microblog.model;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="dt_datarecord")
public class dt_datarecord implements Serializable{

	private static final long serialVersionUID = 1L;
	@Id
	public int datarecord_id;
	public int dataprocess_id;
	public int admin_id;
	public int flag;
	public String jhcode;
	public String age;
	public int number;
	public String planpeople;
	public String people;
	public String text;
	public int createtime;
	public int getDatarecord_id() {
		return datarecord_id;
	}
	public void setDatarecord_id(int datarecord_id) {
		this.datarecord_id = datarecord_id;
	}
	public int getDataprocess_id() {
		return dataprocess_id;
	}
	public void setDataprocess_id(int dataprocess_id) {
		this.dataprocess_id = dataprocess_id;
	}
	public int getAdmin_id() {
		return admin_id;
	}
	public void setAdmin_id(int admin_id) {
		this.admin_id = admin_id;
	}
	public int getFlag() {
		return flag;
	}
	public void setFlag(int flag) {
		this.flag = flag;
	}
	public String getJhcode() {
		return jhcode;
	}
	public void setJhcode(String jhcode) {
		this.jhcode = jhcode;
	}
	public String getAge() {
		return age;
	}
	public void setAge(String age) {
		this.age = age;
	}
	public int getNumber() {
		return number;
	}
	public void setNumber(int number) {
		this.number = number;
	}
	public String getPlanpeople() {
		return planpeople;
	}
	public void setPlanpeople(String planpeople) {
		this.planpeople = planpeople;
	}
	public String getPeople() {
		return people;
	}
	public void setPeople(String people) {
		this.people = people;
	}
	public String getText() {
		return text;
	}
	public void setText(String text) {
		this.text = text;
	}
	public int getCreatetime() {
		return createtime;
	}
	public void setCreatetime(int createtime) {
		this.createtime = createtime;
	}
	
}
