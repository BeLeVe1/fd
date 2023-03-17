package com.hd.microblog.service;

import java.util.List;
import java.util.Map;

import com.hd.common.service.IBaseService;
import com.hd.microblog.model.dt_allotrecord;

public interface dt_allotrecordService extends IBaseService<dt_allotrecord, Integer> {

	List adminfindsupplyplanlist(Integer allot_id,Integer supplyplan_id,Integer selfplan_id,String jqcode,String bdcode,String qccode,String qcname,Integer this_allot_number,Integer plan_supply_number,Integer sum_allot_number,
			String from_store,String to_store,String create_people,Integer createtime,String receive_people,String total_price, String customer_name, String checker,
			String contract, String reviser, String modification_date,
			String preparation_time, String Audit_time,
			String sort,Integer start, int number) ;
	
	List adminfindsupplyplanlist() ;
	
	List adminfindsupplyplanlistcount(Integer allot_id,Integer supplyplan_id,Integer selfplan_id,String jqcode,String bdcode,String qccode,String qcname,Integer this_allot_number,Integer plan_supply_number,Integer sum_allot_number,
			String from_store,String to_store,String create_people,Integer createtime,String receive_people,String total_price, String customer_name, String checker,
			String contract, String reviser, String modification_date,
			String preparation_time, String Audit_time) ;
	
	List sumallotrecord(String bdcode,String qccode,String qcname);
	
	void refreshallotrecord(Integer allot_id,String jqcode,String bdcode,String from_store,String qccode,String qcname,Integer this_allot_number,Integer old_allot_number,Integer sum_allot_number);

	void refreshstorehouse(String jqcode,String from_store,String qccode,String qcname,Integer this_allot_number,Integer old_allot_number);
}
