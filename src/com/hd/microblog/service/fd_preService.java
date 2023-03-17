package com.hd.microblog.service;

import java.util.List;
import java.util.Map;

import com.hd.common.service.IBaseService;
import com.hd.microblog.model.fd_pre;

public interface fd_preService extends IBaseService<fd_pre, Integer> {

	List adminfindfd_prelist(String sort, Integer start, int number,String part_name) ;
	
	
	List adminfindfd_prelistcount(String pre_id,String part_name,String prediction_date,String prediction_value,String running_date
			) ;
	
	
}
