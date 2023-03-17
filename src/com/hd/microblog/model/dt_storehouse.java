package com.hd.microblog.model;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="dt_storehouse")
public class dt_storehouse implements Serializable{
	private static final long serialVersionUID = 1L;
	@Id
	public int dataprocess_id;
	public String jqcode;
	public String bdcode;
	public String zbcode;
	public String qccode;
	public String qcname;
	public String unit;
	public double unitprice;
	public int dzys;
	public int initinventory;
	public int currentinventory;
	
	public int getDataprocess_id() {
		return dataprocess_id;
	}
	public void setDataprocess_id(int dataprocess_id) {
		this.dataprocess_id = dataprocess_id;
	}
	public String getJqcode() {
		return jqcode;
	}
	public void setJqcode(String jqcode) {
		this.jqcode = jqcode;
	}
	public String getBdcode() {
		return bdcode;
	}
	public void setBdcode(String bdcode) {
		this.bdcode = bdcode;
	}
	public String getZbcode() {
		return zbcode;
	}
	public void setZbcode(String zbcode) {
		this.zbcode = zbcode;
	}
	public String getQccode() {
		return qccode;
	}
	public void setQccode(String qccode) {
		this.qccode = qccode;
	}
	public String getQcname() {
		return qcname;
	}
	public void setQcname(String qcname) {
		this.qcname = qcname;
	}
	public String getUnit() {
		return unit;
	}
	public void setUnit(String unit) {
		this.unit = unit;
	}
	public double getUnitprice() {
		return unitprice;
	}
	public void setUnitprice(double unitprice) {
		this.unitprice = unitprice;
	}
	public int getDzys() {
		return dzys;
	}
	public void setDzys(int dzys) {
		this.dzys = dzys;
	}
	public int getInitinventory() {
		return initinventory;
	}
	public void setInitinventory(int initinventory) {
		this.initinventory = initinventory;
	}
	public int getCurrentinventory() {
		return currentinventory;
	}
	public void setCurrentinventory(int currentinventory) {
		this.currentinventory = currentinventory;
	}
}
