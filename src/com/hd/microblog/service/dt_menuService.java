package com.hd.microblog.service;

import java.util.List;
import java.util.Map;

import com.hd.common.service.IBaseService;
import com.hd.microblog.model.dt_menu;


public interface dt_menuService  extends IBaseService<dt_menu, Integer> {

	List adminfindmenulist();

	List adminfindmenulist2(Integer belong);
	
}

