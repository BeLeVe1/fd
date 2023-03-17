package com.hd.microblog.service.impl;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.apache.poi.hssf.usermodel.HSSFCell;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import com.hd.common.dao.IBaseDao;
import com.hd.common.service.impl.BaseService;
import com.hd.microblog.dao.dt_dataprocessDao;
import com.hd.microblog.dao.dt_storehouseDao;
import com.hd.microblog.model.dt_dataprocess;
import com.hd.microblog.model.dt_storehouse;
import com.hd.microblog.service.dt_dataprocessService;
import com.hd.microblog.service.dt_storehouseService;
@Service("dt_storehouseService")

public class dt_storehouseServiceImpl extends BaseService<dt_storehouse, Integer> implements dt_storehouseService{
	private dt_storehouseDao dt_storehousedao;
	@Autowired
	@Qualifier("dt_storehouseDao")
	@Override
	public void setBaseDao(IBaseDao<dt_storehouse, Integer> dt_storehousedao) {
		// TODO Auto-generated method stub
		this.baseDao = dt_storehousedao;
		this.dt_storehousedao = (dt_storehouseDao) dt_storehousedao;
	}
	@Override
	public List adminfindstorehouselist(String jqcode, String bdcode,
			String zbcode, String qccode, String qcname, String sort,
			Integer start, int number) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		String sql = "select * from dt_storehouse where 1=1 ";
		if(jqcode!=""){
			sql+=" and jqcode=? ";
			paramlist.add(jqcode);
			System.out.println(paramlist);
		}
		if(bdcode!=""){
			sql+=" and bdcode=? ";
			paramlist.add(bdcode);
		}
		if(zbcode!=""){
			sql+=" and zbcode=? ";
			paramlist.add(zbcode);
		}
		if(qccode!=""){
			sql+=" and qccode=? ";
			paramlist.add(qccode);
		}
		if(qcname!=""){
			sql+=" and qcname=? ";
			paramlist.add(qcname);
		}
		if(sort!=""){
			sql+=" order by "+sort+" desc ";
		}
		sql += " limit ?, ? ";
		paramlist.add(start);
		paramlist.add(number);
		System.out.println(paramlist);
		return dt_storehousedao.exesqlrelist(sql, paramlist);
	}

	@Override
	public List adminfindstorehouselistcount(String jqcode, String bdcode,
			String zbcode, String qccode, String qcname) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		String sql = "select count(*) count from dt_storehouse where 1=1 ";
		if(jqcode!=""){
			sql+=" and jqcode=? ";
			paramlist.add(jqcode);
		}
		if(bdcode!=""){
			sql+=" and bdcode=? ";
			paramlist.add(bdcode);
		}
		if(zbcode!=""){
			sql+=" and zbcode=? ";
			paramlist.add(zbcode);
		}
		if(qccode!=""){
			sql+=" and qccode=? ";
			paramlist.add(qccode);
		}
		if(qcname!=""){
			sql+=" and qcname=? ";
			paramlist.add(qcname);
		}
		return dt_storehousedao.exesqlrelist(sql, paramlist);
	}
	@Override
	public List adminfindstorehouselist() {
		// TODO Auto-generated method stub
		String sql = "select * from dt_storehouse where 1=1 ";
		return dt_storehousedao.exesqlrelist(sql, null);
	}
	@Override
	public List admindeletestorehouselist() {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		String sql = "delete * from dt_storehouse where 1=1 ";
		dt_storehousedao.exesql(sql, paramlist);
		return null;
	}
	@Override
	public void adminrealsupplyedit() {
		// TODO Auto-generated method stub
		
	}
	@Override
	public List desstorecount(String jqcode, String desbdcode, String qccode,
			String qcname) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		String sql = "select * from dt_storehouse where bdcode="+desbdcode+" and jqcode="+jqcode+" and qccode="+qccode+" and qcname= '"+qcname+"' ";		
		String sql1 = "select * from dt_storehouse where bdcode="+desbdcode+" and jqcode="+jqcode+" and qccode="+qccode+" and qcname= '"+qcname+"'";		
		return dt_storehousedao.exesqlrelist(sql1, paramlist);
	}
	@Override
	public void updatestorehouse(String jqcode, String bdcode,
			String desbdcode, String qccode, String qcname, Integer new_store,
			Integer old_store) {
		// TODO Auto-generated method stub
		String sql = "update dt_storehouse set currentinventory="+new_store+" where bdcode="+desbdcode+" and jqcode="+jqcode+" and qccode="+qccode+" ";
		String sql1 = "update dt_storehouse set currentinventory="+old_store+" where bdcode="+bdcode+" and jqcode="+jqcode+" and qccode="+qccode+" ";
		dt_storehousedao.addSumplan(sql);
		dt_storehousedao.addSumplan(sql1);
		System.out.println(sql);
		System.out.println(sql1);
	}
	@Override
	public void insertstorehouse(String jqcode, String bdcode,
			String desbdcode, String zbcode,String qccode, String qcname, String unit,String unitprice,String dzys,Integer new_store,
			Integer old_store) {
		// TODO Auto-generated method stub
		String sql = "insert into dt_storehouse(initinventory,currentinventory,bdcode,jqcode,zbcode,qccode,qcname,unit,unitprice,dzys) values(0,'"+new_store+"','"+desbdcode+"','"+jqcode+"','"+zbcode+"','"+qccode+"','"+qcname+"','"+unit+"','"+unitprice+"','"+dzys+"')";
		//String sql0 = "update dt_storehouse set zbcode="+old_store+" where bdcode="+bdcode+" and jqcode="+jqcode+" and qccode="+qccode+" and qcname='"+qcname+"'";
		//String sql = "insert dt_storehouse set currentinventory="+new_store+" where bdcode="+desbdcode+" and jqcode="+jqcode+" and qccode="+qccode+" and qcname="+qcname+"";
		String sql1 = "update dt_storehouse set currentinventory="+old_store+" where bdcode="+bdcode+" and jqcode="+jqcode+" and qccode="+qccode+" and qcname='"+qcname+"'";
		dt_storehousedao.addSumplan(sql);
		dt_storehousedao.addSumplan(sql1);
		System.out.println(sql);
		System.out.println(sql1);
	}
	@Override
	public List querybdcode(String jqcode,String qccode) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		String sql1 = "select bdcode,currentinventory from dt_storehouse where jqcode="+jqcode+" and qccode="+qccode+"";		
		return dt_storehousedao.exesqlrelist(sql1, paramlist);
	}
	@Override
	public void insertstorerecord(String jqcode, String bdcode,
			String desbdcode, String zbcode, String qccode, String qcname,
			Integer recordnumber, String create_people, String createtime,
			String receive_people) {
		// TODO Auto-generated method stub
		String sql = "insert into dt_store_datarecordlist(jqcode,from_store,to_store,zbcode,qccode,qcname,this_allot_number,create_people,createtime,receive_people) values('"+jqcode+"','"+bdcode+"','"+desbdcode+"','"+zbcode+"','"+qccode+"','"+qcname+"','"+recordnumber+"','"+create_people+"','"+createtime+"','"+receive_people+"')";
		dt_storehousedao.addSumplan(sql);
		System.out.println(sql);
	}
	@Override
	public List adminfindstorerecordlist(String jqcode, String from_store,
			String to_store, String qccode, String qcname, String sort,
			Integer start, int number) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		String sql = "select * from dt_store_datarecordlist where 1=1 ";
		if(jqcode!=""){
			sql+=" and jqcode=? ";
			paramlist.add(jqcode);
			System.out.println(paramlist);
		}
		if(from_store!=""){
			sql+=" and from_store=? ";
			paramlist.add(from_store);
		}
		if(to_store!=""){
			sql+=" and to_store=? ";
			paramlist.add(to_store);
		}
		if(qccode!=""){
			sql+=" and qccode=? ";
			paramlist.add(qccode);
		}
		if(qcname!=""){
			sql+=" and qcname=? ";
			paramlist.add(qcname);
		}
		if(sort!=""){
			sql+=" order by "+sort+" desc ";
		}
		sql += " limit ?, ? ";
		paramlist.add(start);
		paramlist.add(number);
		System.out.println(paramlist);
		return dt_storehousedao.exesqlrelist(sql, paramlist);
	}
	@Override
	public List adminfindstorerecordlistcount(String jqcode, String from_store,
			String to_store, String qccode, String qcname) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		String sql = "select count(*) count from dt_store_datarecordlist where 1=1 ";
		if(jqcode!=""){
			sql+=" and jqcode=? ";
			paramlist.add(jqcode);
		}
		if(from_store!=""){
			sql+=" and from_store=? ";
			paramlist.add(from_store);
		}
		if(to_store!=""){
			sql+=" and to_store=? ";
			paramlist.add(to_store);
		}
		if(qccode!=""){
			sql+=" and qccode=? ";
			paramlist.add(qccode);
		}
		if(qcname!=""){
			sql+=" and qcname=? ";
			paramlist.add(qcname);
		}
		return dt_storehousedao.exesqlrelist(sql, paramlist);
	}
	@Override
	public void refreshstorerecord(Integer allot_id,String jqcode, String from_store,
			String to_store, String qccode, String qcname,
			Integer this_allot_number, Integer old_allot_number) {
		// TODO Auto-generated method stub
		//更新当次的调拨量
		String sql = "update dt_store_datarecordlist set this_allot_number="+this_allot_number+" where allot_id='"+allot_id+"' and jqcode='"+jqcode+"' and from_store='"+from_store+"' and to_store='"+to_store+"' and qccode='"+qccode+"' and qcname='"+qcname+"'";
		dt_storehousedao.addSumplan(sql);
		//更新相关记录的所有累计调拨量
		if(old_allot_number>this_allot_number){
			Integer differ_allotnumber=old_allot_number-this_allot_number;
			//旧的调拨数量更大，to_store减少
			String sql2 = "update dt_storehouse set currentinventory=currentinventory-"+differ_allotnumber+" where jqcode='"+jqcode+"' and bdcode='"+to_store+"' and qccode='"+qccode+"' and qcname='"+qcname+"'";
			//from_store增加,注意仓库的bdcode是指的仓库号，不是部队号！
			String sql3 = "update dt_storehouse set currentinventory=currentinventory+"+differ_allotnumber+" where jqcode='"+jqcode+"' and bdcode='"+from_store+"' and qccode='"+qccode+"' and qcname='"+qcname+"'";
			dt_storehousedao.addSumplan(sql2);
			dt_storehousedao.addSumplan(sql3);
		}else{
			Integer differ_allotnumber=this_allot_number-old_allot_number;
			//旧的调拨数量更小，to_store增加
			String sql2 = "update dt_storehouse set currentinventory=currentinventory+"+differ_allotnumber+" where jqcode='"+jqcode+"' and bdcode='"+to_store+"' and qccode='"+qccode+"' and qcname='"+qcname+"'";
			//from_store减少,注意仓库的bdcode是指的仓库号，不是部队号！
			String sql3 = "update dt_storehouse set currentinventory=currentinventory-"+differ_allotnumber+" where jqcode='"+jqcode+"' and bdcode='"+from_store+"' and qccode='"+qccode+"' and qcname='"+qcname+"'";
			dt_storehousedao.addSumplan(sql2);
			dt_storehousedao.addSumplan(sql3);
		}
		System.out.println("执行完了");
	}
	@Override
	public List adminfindstorerecordlist() {
		// TODO Auto-generated method stub
		String sql = "select * from dt_store_datarecordlist where 1=1 ";
		return dt_storehousedao.exesqlrelist(sql, null);
	}
	
}
