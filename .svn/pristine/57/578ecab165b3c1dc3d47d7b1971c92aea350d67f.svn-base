package com.hd.microblog.service.impl;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import com.hd.common.dao.IBaseDao;
import com.hd.common.service.impl.BaseService;
import com.hd.microblog.dao.dt_menuDao;
import com.hd.microblog.model.dt_menu;
import com.hd.microblog.service.dt_menuService;
@Service("dt_menuService")
public class dt_menuServiceImpl extends BaseService<dt_menu, Integer> implements dt_menuService{
	private dt_menuDao dt_menudao;
	@Autowired
	@Qualifier("dt_menuDao")
	@Override
	public void setBaseDao(IBaseDao<dt_menu, Integer> dt_menudao) {
		this.baseDao = dt_menudao;
		this.dt_menudao = (dt_menuDao) dt_menudao;
	}
	@Override
	public List adminfindmenulist() {
		// TODO Auto-generated method stub
		String sql = "select * from dt_menu where type=0 order by order_num asc ";
		return dt_menudao.exesqlrelist(sql, null);
	}
	@Override
	public List adminfindmenulist2(Integer belong) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		String sql = "select * from dt_menu where type=1 and belong=? order by order_num asc ";
		paramlist.add(belong);
		return dt_menudao.exesqlrelist(sql, paramlist);
	}
}
