package com.hd.microblog.service;

import java.util.List;
import java.util.Map;

import com.hd.common.service.IBaseService;
import com.hd.microblog.model.dt_amount;


public interface dt_amountService  extends IBaseService<dt_amount, Integer> {

	List adminfindamountlist(String zbcode,String zbname,String sort,Integer start, int number);

	List adminfindamountlistcount(String zbcode,String zbname);

	List adminfindamountlist();

	List adminfindamountlistAll();
	
}

