package com.hd.microblog.service.impl;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

import org.apache.poi.hssf.usermodel.HSSFCell;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import com.hd.common.dao.IBaseDao;
import com.hd.common.service.impl.BaseService;
import com.hd.microblog.dao.fd_preDao;
import com.hd.microblog.model.fd_pre;
import com.hd.microblog.service.fd_preService;

@Service("fd_preService")
public class fd_preServicelmpl extends BaseService<fd_pre, Integer> implements fd_preService{

	
	private fd_preDao fd_predao;
	@Autowired
	@Qualifier("fd_preDao")
	@Override
	public void setBaseDao(IBaseDao<fd_pre, Integer> fd_predao) {
		// TODO Auto-generated method stub
		this.baseDao = fd_predao;
		this.fd_predao = (fd_preDao) fd_predao;
	}
		
	@Override
	public List adminfindfd_prelist(String sort, Integer start, int number,String part_name)  {
		// TODO Auto-generated method stub
        String sql = "select * from fd_pre where 1=1 ";
		
		
		List<Object> paramlist = new ArrayList();
		if(part_name!=""){
			sql+=" and part_name=? ";
			paramlist.add(part_name);
		}
		if(sort!=""){
			sql+=" order by "+sort+" desc ";
		}
		sql += " limit ?, ? ";
		paramlist.add(start);
		paramlist.add(number);
		System.out.println(paramlist);
		System.out.printf("sql代码为：");
		System.out.printf(sql);
		return fd_predao.exesqlrelist(sql, paramlist);
		
	}

	@Override
	public List adminfindfd_prelistcount(String pre_id,String part_name,String prediction_date,String prediction_value,String running_date
			) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		String sql = "select count(*) count from dt_datarecordlist where 1=1 ";
		System.out.println("shenmegui");
		System.out.println(paramlist);
		System.out.printf("sql代码为：",sql);
		return fd_predao.exesqlrelist(sql, paramlist);
	}



}
