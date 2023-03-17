package com.hd.microblog.service.impl;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import com.hd.common.dao.IBaseDao;
import com.hd.common.service.impl.BaseService;
import com.hd.microblog.dao.dt_amountDao;
import com.hd.microblog.model.dt_amount;
import com.hd.microblog.service.dt_amountService;
@Service("dt_amountService")
public class dt_amountServiceImpl extends BaseService<dt_amount, Integer> implements dt_amountService{
	private dt_amountDao dt_amountdao;
	@Autowired
	@Qualifier("dt_amountDao")
	@Override
	public void setBaseDao(IBaseDao<dt_amount, Integer> dt_amountdao) {
		this.baseDao = dt_amountdao;
		this.dt_amountdao = (dt_amountDao) dt_amountdao;
	}
	@Override
	public List adminfindamountlist(String zbcode,String zbname,String sort,Integer start, int number) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		String sql = "select * from dt_amount where 1=1 ";
		if(zbcode!=""){
			sql+=" and zbcode=? ";
			paramlist.add(zbcode);
		}
		if(zbname!=""){
			sql+=" and zbname=? ";
			paramlist.add(zbname);
		}
		if(sort!=""){
			sql+=" order by "+sort+" desc ";
		}
		sql += " limit ?, ? ";
		paramlist.add(start);
		paramlist.add(number);
		return dt_amountdao.exesqlrelist(sql, paramlist);
	}
	@Override
	public List adminfindamountlistcount(String zbcode,String zbname) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		String sql = "select count(*) count from dt_amount where 1=1 ";
		if(zbcode!=""){
			sql+=" and zbcode=? ";
			paramlist.add(zbcode);
		}
		if(zbname!=""){
			sql+=" and zbname=? ";
			paramlist.add(zbname);
		}
		return dt_amountdao.exesqlrelist(sql, paramlist);
	}
	@Override
	public List adminfindamountlist() {
		// TODO Auto-generated method stub
		String sql = "select * from dt_amount where 1=1 ";
		return dt_amountdao.exesqlrelist(sql, null);
	}
	@Override
	public List adminfindamountlistAll() {
		// TODO Auto-generated method stub
		String sql = "select * from dt_amount where 1=1 ";
		return dt_amountdao.exesqlrelist(sql, null);
	}
}
