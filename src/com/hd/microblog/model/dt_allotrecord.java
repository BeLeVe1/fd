package com.hd.microblog.model;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="dt_allotrecord")

public class dt_allotrecord implements Serializable{
	private static final long serialVersionUID = 1L;
	@Id
	public int allot_id;
	public int supplyplan_id;
	public int selfplan_id;
	public String jqcode;
	public String bdcode;
	public String qccode;
	public String qcname;
	
	public int this_allot_number;
	public int plan_supply_number;
	public int sum_allot_number;
	
	public String from_store;
	public String to_store;
	public String create_people;
	public int createtime;
	public String receive_people;
	
	public String total_price;
	public String customer_name;
	public String checker;
	public String contract;
	public String reviser;
	public String modification_date;
	public String preparation_time;
	public String Audit_time;
	
	
	public int sort;
	public int start;
	public int number;
	
	public int getSupplyplan_id() {
		return supplyplan_id;
	}
	public void setSupplyplan_id(int supplyplan_id) {
		this.supplyplan_id = supplyplan_id;
	}
	
	public int getSelfplan_id() {
		return selfplan_id;
	}
	public void setSelfplan_id(int selfplan_id) {
		this.selfplan_id = selfplan_id;
	}
	
	public String getQcname() {
		return qcname;
	}
	public void setQcname(String qcname) {
		this.qcname = qcname;
	}
	
	public String getQccode() {
		return qccode;
	}
	public void setQccode(String qccode) {
		this.qccode = qccode;
	}
	
	public int getThis_allot_number() {
		return this_allot_number;
	}
	public void setThis_allot_number(int this_allot_number) {
		this.this_allot_number = this_allot_number;
	}
	
	public int getPlan_supply_number() {
		return plan_supply_number;
	}
	public void setPlan_supply_number(int plan_supply_number) {
		this.plan_supply_number = plan_supply_number;
	}
	
	public int getSum_allot_number() {
		return sum_allot_number;
	}
	public void setSum_allot_number(int sum_allot_number) {
		this.sum_allot_number = sum_allot_number;
	}
	
	public String getFrom_store() {
		return from_store;
	}
	public void setFrom_store(String from_store) {
		this.from_store = from_store;
	}
	
	public String getTo_store() {
		return to_store;
	}
	public void setTo_store(String to_store) {
		this.to_store = to_store;
	}
	
	public String getCreate_people() {
		return create_people;
	}
	public void setCreate_people(String create_people) {
		this.create_people = create_people;
	}
	
	public String getReceive_people() {
		return receive_people;
	}
	public void settotal_price(String total_price) {
		this.total_price = total_price;
	}
	public void setcustomer_name(String customer_name) {
		this.customer_name = customer_name;
	}
	public void setchecker(String checker) {
		this.checker = checker;
	}
	public void setcontract(String contract) {
		this.contract = contract;
	}
	public void setreviser(String reviser) {
		this.reviser = reviser;
	}
	public void setmodification_date(String modification_date) {
		this.modification_date = modification_date;
	}
	public void setReceive_people(String receive_people) {
		this.receive_people = receive_people;
	}
	public void setpreparation_time(String preparation_time) {
		this.preparation_time = preparation_time;
	}
	public void setAudit_time(String Audit_time) {
		this.Audit_time = Audit_time;
	}
	public int getCreatetime() {
		return createtime;
	}
	public void setCreatetime(int createtime) {
		this.createtime = createtime;
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
