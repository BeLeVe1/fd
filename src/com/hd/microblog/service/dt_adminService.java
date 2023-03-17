package com.hd.microblog.service;

import java.util.List;
import java.util.Map;

import com.hd.common.service.IBaseService;
import com.hd.microblog.model.dt_admin;


public interface dt_adminService  extends IBaseService<dt_admin, Integer> {

	List adminfindaccount(String account);

	List adminfindadminlist(Integer start, int number);

	List adminfindadminlistcount();
	
}

