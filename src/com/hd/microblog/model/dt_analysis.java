package com.hd.microblog.model;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="dt_analysis")
public class dt_analysis implements Serializable{

	private static final long serialVersionUID = 1L;
	@Id
	public int analysis_id;
	public int dataprocess_id;
	public String ycff;
	public String ycz;
	public String bzc;
	public String ycfxt;
	public int getAnalysis_id() {
		return analysis_id;
	}
	public void setAnalysis_id(int analysis_id) {
		this.analysis_id = analysis_id;
	}
	public int getDataprocess_id() {
		return dataprocess_id;
	}
	public void setDataprocess_id(int dataprocess_id) {
		this.dataprocess_id = dataprocess_id;
	}
	public String getYcff() {
		return ycff;
	}
	public void setYcff(String ycff) {
		this.ycff = ycff;
	}
	public String getYcz() {
		return ycz;
	}
	public void setYcz(String ycz) {
		this.ycz = ycz;
	}
	public String getBzc() {
		return bzc;
	}
	public void setBzc(String bzc) {
		this.bzc = bzc;
	}
	public String getYcfxt() {
		return ycfxt;
	}
	public void setYcfxt(String ycfxt) {
		this.ycfxt = ycfxt;
	}
	public static long getSerialversionuid() {
		return serialVersionUID;
	}
	
}
