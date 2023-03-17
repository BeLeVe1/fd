package com.hd.microblog.service;

import java.util.List;
import java.util.Map;

import com.hd.common.service.IBaseService;
import com.hd.microblog.model.dt_plan;


public interface dt_planService  extends IBaseService<dt_plan, Integer> {

	List adminfindplanlist(String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg,String sort,Integer start, int number);

	List adminfindplanlistcount(String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg);
	
	List adminfindplanlistcount3(String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg);

	List adminfindplanlist(String fg);
	
	List adminfindsupplyplanlist(String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg,String sort,Integer start, int number);
	
	List adminfindsupplyplanlistcount(String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg);
	
	List adminfindsupplyplanlist(String fg);
	
	List adminfindapplyplanlist(String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg,String sort,Integer start, int number);
	
	List adminfindapplyplanlistcount(String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg);
	
	List adminfindapplyplanlist(String fg);
	
	void adminfindsumplanlist();
	
	void adminrealsupplyedit(String bdcode,String qccode,String qcname,String fg,Integer realsupply,String comments);
	
	void adminselfsupplyplanedit(String jqcode,String bdcode,String qccode,String qcname,String fg,Integer realnumber,String comments);
	
	void adminallotrecord(Integer recordnumber,String sharedpart_id,String jqcode,String bdcode,String qccode,String qcname,Integer realsupply,String create_people,String createtime,String receive_people,String fg,Integer sum_allot_number,String desbdcode);
	
	void refreshstorehouse(String sharedpart_id,String desbdcode,String jqcode,String bdcode,String qccode,String qcname,Integer remain_store,Integer storehouse_remain_store);
}

