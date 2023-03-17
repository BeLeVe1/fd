package com.hd.microblog.service;

import java.util.List;
import java.util.Map;

import org.apache.poi.hssf.usermodel.HSSFCell;

import com.hd.common.service.IBaseService;
import com.hd.microblog.model.dt_storehouse;

public interface dt_storehouseService extends IBaseService<dt_storehouse, Integer> {

	List adminfindstorehouselist(String jqcode, String bdcode, String zbcode,
			String qccode, String qcname, String sort,
			Integer start, int number);
	
	List adminfindstorehouselist();
	
	List adminfindstorerecordlist();
	
	List adminfindstorehouselistcount(String jqcode, String bdcode,
			String zbcode, String qccode, String qcname);
	
	List adminfindstorerecordlist(String jqcode, String from_store,String to_store,
			String qccode, String qcname, String sort,
			Integer start, int number);
	
	List adminfindstorerecordlistcount(String jqcode, String from_store,
			String to_store, String qccode, String qcname);
	
	//读取目标仓库库存
	List desstorecount(String jqcode, String desbdcode, String qccode, String qcname);
	//更新目标仓库
	void updatestorehouse(String jqcode, String bdcode,String desbdcode,String qccode, String qcname,Integer new_store,Integer old_store);	
	//插入目标仓库
	void insertstorehouse(String jqcode, String bdcode,String desbdcode,String zbcode,String qccode, String qcname,String unit,String unitprice,String dzys,Integer new_store,Integer old_store);
	//生成仓库调拨记录
	void insertstorerecord(String jqcode, String bdcode,String desbdcode,String zbcode,String qccode, String qcname,Integer recordnumber,String create_people,String createtime,String receive_people);
	
	List admindeletestorehouselist();
	//这个是干嘛的来着？
	void adminrealsupplyedit();
	
	void refreshstorerecord(Integer allot_id,String jqcode,String from_store,String to_store,
			String qccode,String qcname,Integer this_allot_number,Integer old_allot_number);

	List querybdcode(String jqcode,String qccode);
	
}
