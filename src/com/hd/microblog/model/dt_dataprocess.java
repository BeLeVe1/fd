package com.hd.microblog.model;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="dt_dataprocess")
public class dt_dataprocess implements Serializable{

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
	public String fg;
	public double age1;
	public double age2;
	public double age3;
	public double age4;
	public double age5;
	public double age6;
	public double age7;
	public double age8;
	public double age9;
	public double age10;
	public int ycff;
	public double anumber;
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
	public String getFg() {
		return fg;
	}
	public void setFg(String fg) {
		this.fg = fg;
	}
	public double getAge1() {
		return age1;
	}
	public void setAge1(double age1) {
		this.age1 = age1;
	}
	public double getAge2() {
		return age2;
	}
	public void setAge2(double age2) {
		this.age2 = age2;
	}
	public double getAge3() {
		return age3;
	}
	public void setAge3(double age3) {
		this.age3 = age3;
	}
	public double getAge4() {
		return age4;
	}
	public void setAge4(double age4) {
		this.age4 = age4;
	}
	public double getAge5() {
		return age5;
	}
	public void setAge5(double age5) {
		this.age5 = age5;
	}
	public double getAge6() {
		return age6;
	}
	public void setAge6(double age6) {
		this.age6 = age6;
	}
	public double getAge7() {
		return age7;
	}
	public void setAge7(double age7) {
		this.age7 = age7;
	}
	public double getAge8() {
		return age8;
	}
	public void setAge8(double age8) {
		this.age8 = age8;
	}
	public double getAge9() {
		return age9;
	}
	public void setAge9(double age9) {
		this.age9 = age9;
	}
	public double getAge10() {
		return age10;
	}
	public void setAge10(double age10) {
		this.age10 = age10;
	}
	public int getYcff() {
		return ycff;
	}
	public void setYcff(int ycff) {
		this.ycff = ycff;
	}
	public double getAnumber() {
		return anumber;
	}
	public void setAnumber(double anumber) {
		this.anumber = anumber;
	}
	
}
