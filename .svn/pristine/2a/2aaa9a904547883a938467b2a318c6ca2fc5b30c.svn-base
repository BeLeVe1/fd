package com.hd.microblog.service.impl;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import com.hd.common.dao.IBaseDao;
import com.hd.common.service.impl.BaseService;
import com.hd.microblog.dao.dt_adminDao;
import com.hd.microblog.model.dt_admin;
import com.hd.microblog.service.dt_adminService;
@Service("dt_adminService")
public class dt_adminServiceImpl extends BaseService<dt_admin, Integer> implements dt_adminService{
	private dt_adminDao dt_admindao;
	@Autowired
	@Qualifier("dt_adminDao")
	@Override
	public void setBaseDao(IBaseDao<dt_admin, Integer> dt_admindao) {
		this.baseDao = dt_admindao;
		this.dt_admindao = (dt_adminDao) dt_admindao;
	}
	@Override
	public List adminfindaccount(String account) {
		// TODO Auto-generated method stub
		String sql = "From dt_admin where account=? and status=1 ";
		List<Object> paramlist = new ArrayList();
		paramlist.add(account);
		return dt_admindao.exehqlrelist(sql, paramlist);
	}
	@Override
	public List adminfindadminlist(Integer start, int number) {
		// TODO Auto-generated method stub
		String sql = "select * from dt_admin where status<2 and 1=1 ";
		sql += " limit ?, ? ";
		List<Object> paramlist = new ArrayList();
		paramlist.add(start);
		paramlist.add(number);
		return dt_admindao.exesqlrelist(sql, paramlist);
	}
	@Override
	public List adminfindadminlistcount() {
		// TODO Auto-generated method stub
		String sql = "select count(*) count from dt_admin where status<2 and 1=1 ";
		return dt_admindao.exesqlrelist(sql, null);
	}
}
