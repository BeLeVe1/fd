package com.hd.microblog.service.impl;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import com.hd.common.dao.IBaseDao;
import com.hd.common.service.impl.BaseService;
import com.hd.microblog.dao.dt_planDao;
import com.hd.microblog.model.dt_plan;
import com.hd.microblog.service.dt_planService;
@Service("dt_planService")
public class dt_planServiceImpl extends BaseService<dt_plan, Integer> implements dt_planService{
	private dt_planDao dt_plandao;
	@Autowired
	@Qualifier("dt_planDao")
	@Override
	public void setBaseDao(IBaseDao<dt_plan, Integer> dt_plandao) {
		this.baseDao = dt_plandao;
		this.dt_plandao = (dt_planDao) dt_plandao;
	}
	@Override
	public List adminfindplanlist(String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg,String sort,Integer start, int number) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		//String sql = "select d.*,p.plan_id,s.sharedpart_id,s.predictionnumber,s.plannumber,s.maxnumber,s.kyd,p.number,s.realnumber from dt_dataprocess d left join dt_plan p on d.dataprocess_id=p.dataprocess_id left join dt_sharedpart s on d.dataprocess_id=s.dataprocess_id where 1=1 ";
		String sql = "select d.* from dt_sumplan d where 1=1";
		if(jqcode!=""){
			sql+=" and d.jqcode=? ";
			paramlist.add(jqcode);
		}
		if(bdcode!=""){
			sql+=" and d.bdcode=? ";
			paramlist.add(bdcode);
		}
		if(zbcode!=""){
			sql+=" and d.zbcode=? ";
			paramlist.add(zbcode);
		}
		if(qccode!=""){
			sql+=" and d.qccode=? ";
			paramlist.add(qccode);
		}
		if(qcname!=""){
			sql+=" and d.qcname=? ";
			paramlist.add(qcname);
		}
		if(fg!=""){
			sql+=" and d.fg=? ";
			paramlist.add(fg);
		}
		if(sort!=""){
			if(sort.equals("predictionnumber")||sort.equals("plannumber")) {
				sql+=" order by s."+sort+" desc ";
			}else{
				sql+=" order by p."+sort+" desc ";
			}
		}else {
			sql+=" order by d.qccode asc,d.jqcode asc ";
		}
		sql += " limit ?, ? ";
		paramlist.add(start);
		paramlist.add(number);
		return dt_plandao.exesqlrelist(sql, paramlist);
	}
	@Override
	public List adminfindplanlistcount(String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		//String sql = "select count(*) count from dt_dataprocess where 1=1 ";
		String sql = "select count(*) count from dt_sumplan where 1=1 ";
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
		if(fg!=""){
			sql+=" and fg=? ";
			paramlist.add(fg);
		}
		return dt_plandao.exesqlrelist(sql, paramlist);
	}
	
	@Override
	public List adminfindplanlistcount3(String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		//String sql = "select count(*) count from dt_dataprocess where 1=1 ";
		String sql = "select count(*) count from dt_sumplan where 1=1 ";
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
		if(fg!=""){
			sql+=" and fg=? ";
			paramlist.add(fg);
		}
		return dt_plandao.exesqlrelist(sql, paramlist);
	}
	
	@Override
	public List adminfindplanlist(String fg) {
		// TODO Auto-generated method stub
		//String sql = "select d.*,p.plan_id,s.sharedpart_id,s.predictionnumber,s.plannumber,s.maxnumber,s.kyd,p.number,s.realnumber from dt_dataprocess d left join dt_plan p on d.dataprocess_id=p.dataprocess_id left join dt_sharedpart s on d.dataprocess_id=s.dataprocess_id where d.fg='"+fg+"' ";
		String sql = "select d.* from dt_sumplan d where 1=1";
		sql+=" order by d.qccode asc,d.jqcode asc ";
		return dt_plandao.exesqlrelist(sql, null);
	}
	
	@Override
	public List adminfindapplyplanlist(String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg,String sort,Integer start, int number) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		//String sql = "select d.*,p.plan_id,s.sharedpart_id,s.predictionnumber,s.plannumber,s.maxnumber,s.kyd,p.number,s.realnumber from dt_dataprocess d left join dt_plan p on d.dataprocess_id=p.dataprocess_id left join dt_sharedpart s on d.dataprocess_id=s.dataprocess_id where 1=1 ";
		String sql = "select d.* from dt_sumplan d where 1=1";
		if(jqcode!=""){
			sql+=" and d.jqcode=? ";
			paramlist.add(jqcode);
		}
		if(bdcode!=""){
			sql+=" and d.bdcode=? ";
			paramlist.add(bdcode);
		}
		if(zbcode!=""){
			sql+=" and d.zbcode=? ";
			paramlist.add(zbcode);
		}
		if(qccode!=""){
			sql+=" and d.qccode=? ";
			paramlist.add(qccode);
		}
		if(qcname!=""){
			sql+=" and d.qcname=? ";
			paramlist.add(qcname);
		}
		if(fg!=""){
			sql+=" and d.fg!=? ";
			paramlist.add(fg);
		}
		if(sort!=""){
			if(sort.equals("predictionnumber")||sort.equals("plannumber")) {
				sql+=" order by s."+sort+" desc ";
			}else{
				sql+=" order by p."+sort+" desc ";
			}
		}else {
			sql+=" order by d.qccode asc,d.jqcode asc ";
		}
		sql += " limit ?, ? ";
		paramlist.add(start);
		paramlist.add(number);
		return dt_plandao.exesqlrelist(sql, paramlist);
	}
	
	@Override
	public List adminfindapplyplanlistcount(String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		//String sql = "select count(*) count from dt_dataprocess where 1=1 ";
		String sql = "select count(*) count from dt_sumplan where 1=1 ";
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
		if(fg!=""){
			sql+=" and fg!=? ";
			paramlist.add(fg);
		}
		return dt_plandao.exesqlrelist(sql, paramlist);
	}
	
	@Override
	public List adminfindapplyplanlist(String fg) {
		// TODO Auto-generated method stub
		//String sql = "select d.*,p.plan_id,s.sharedpart_id,s.predictionnumber,s.plannumber,s.maxnumber,s.kyd,p.number,s.realnumber from dt_dataprocess d left join dt_plan p on d.dataprocess_id=p.dataprocess_id left join dt_sharedpart s on d.dataprocess_id=s.dataprocess_id where d.fg='"+fg+"' ";
		String sql = "select d.* from dt_sumplan d where 1=1";
		sql+=" order by d.qccode asc,d.jqcode asc ";
		return dt_plandao.exesqlrelist(sql, null);
	}
	
	@Override
	public List adminfindsupplyplanlist(String jqcode, String bdcode,
			String zbcode, String qccode, String qcname, String fg,
			String sort, Integer start, int number) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		//String sql = "select d.*,p.plan_id,s.predictionnumber,s.plannumber,p.number,(s.predictionnumber-p.number) as makingplansnumber,p.thistimeplansnumber,s.maxnumber,s.kyd,(s.plannumber-p.number) as lastnumber from dt_dataprocess d left join dt_plan p on d.dataprocess_id=p.dataprocess_id left join dt_sharedpart s on d.dataprocess_id=s.dataprocess_id where 1=1";
		String sql = "select d.* from dt_sumplan d where 1=1";
		if(jqcode!=""){
			sql+=" and d.jqcode=? ";
			paramlist.add(jqcode);
		}
		if(bdcode!=""){
			sql+=" and d.bdcode=? ";
			paramlist.add(bdcode);
		}
		if(zbcode!=""){
			sql+=" and d.zbcode=? ";
			paramlist.add(zbcode);
		}
		if(qccode!=""){
			sql+=" and d.qccode=? ";
			paramlist.add(qccode);
		}
		if(qcname!=""){
			sql+=" and d.qcname=? ";
			paramlist.add(qcname);
		}
		if(fg!=""){
			sql+=" and d.fg!=? ";
			paramlist.add(fg);
		}
		if(sort!=""){
			if(sort.equals("predictionnumber")||sort.equals("plannumber")) {
				sql+=" order by s."+sort+" desc ";
			}else{
				sql+=" order by p."+sort+" desc ";
			}
		}else {
			sql+=" order by d.qccode asc,d.jqcode asc ";
		}
		sql += " limit ?, ? ";
		paramlist.add(start);
		paramlist.add(number);
		return dt_plandao.exesqlrelist(sql, paramlist);
	}
	@Override
	public List adminfindsupplyplanlistcount(String jqcode, String bdcode,
			String zbcode, String qccode, String qcname, String fg) {
		// TODO Auto-generated method stub
		List<Object> paramlist = new ArrayList();
		String sql = "select count(*) count from dt_sumplan where 1=1 ";
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
		if(fg!=""){
			sql+=" and fg!=? ";
			paramlist.add(fg);
		}
		return dt_plandao.exesqlrelist(sql, paramlist);
	}
	@Override
	public List adminfindsupplyplanlist(String fg) {
		// TODO Auto-generated method stub
		//String sql = "select d.*,p.plan_id,s.predictionnumber,s.plannumber,p.number,(s.predictionnumber-p.number) as makingplansnumber,p.thistimeplansnumber,s.maxnumber,s.kyd,(s.plannumber-p.number) as lastnumber from dt_dataprocess d left join dt_plan p on d.dataprocess_id=p.dataprocess_id left join dt_sharedpart s on d.dataprocess_id=s.dataprocess_id where 1=1";
		String sql = "select d.* from dt_sumplan d where 1=1";
		sql+=" order by d.qccode asc,d.jqcode asc ";
		return dt_plandao.exesqlrelist(sql, null);
	}
	@Override
	public void adminfindsumplanlist() {
		// TODO Auto-generated method stub
		String sql1 = "truncate table dt_sumplan";
		String sql = "insert into dt_sumplan(dataprocess_id,predictionnumber,plannumber,realsupply,jqcode,bdcode,zbcode,qccode,qcname,initinventory,currentinventory,fg) select s.sharedpart_id,s.predictionnumber,s.plannumber,s.realnumber,d.jqcode,d.bdcode,d.zbcode,d.qccode,d.qcname,st.initinventory,st.currentinventory,d.fg from dt_sharedpart s left join dt_dataprocess d on s.sharedpart_id=d.dataprocess_id left join dt_storehouse st on d.bdcode=st.bdcode and d.qccode=st.qccode and d.qcname=st.qcname";
		String sqll = "update dt_sumplan su set su.currentinventory = (select sum(st.currentinventory) from dt_storehouse st where st.jqcode=su.jqcode and st.bdcode=su.bdcode and st.qccode=su.qccode) where exists (select sum(st.currentinventory) from dt_storehouse st where st.jqcode=su.jqcode and st.bdcode=su.bdcode and st.qccode=su.qccode)";
		String sqlll = "update dt_sumplan su set su.initinventory = (select sum(st.initinventory) from dt_storehouse st where st.jqcode=su.jqcode and st.bdcode=su.bdcode and st.qccode=su.qccode) where exists (select sum(st.initinventory) from dt_storehouse st where st.jqcode=su.jqcode and st.bdcode=su.bdcode and st.qccode=su.qccode)";
		//String sql = "insert into dt_sumplan(dataprocess_id,predictionnumber,plannumber,realsupply,jqcode,bdcode,zbcode,qccode,qcname,initinventory,currentinventory,fg) select s.sharedpart_id,s.predictionnumber,s.plannumber,s.realnumber,d.jqcode,d.bdcode,d.zbcode,d.qccode,d.qcname,sum(st.initinventory),sum(st.currentinventory),d.fg from dt_sharedpart s left join dt_dataprocess d on s.sharedpart_id=d.dataprocess_id left join dt_storehouse st on d.jqcode=st.jqcode and d.qccode=st.qccode and d.qcname=st.qcname";
		String sql2 = "update dt_sumplan set type='消耗件' where type is null";
		String sql33 = "insert into dt_sumplan(predictionnumber,plannumber,realsupply,jqcode,bdcode,zbcode,qccode,qcname,fg) select number,number,number,armyid,armyid,mitemid,itemid,itemname,fg from sp_item where number is not null";
		String sql4 = "update dt_sumplan set type='可修件' where type is null";
		String sql5 = "update dt_sumplan set initinventory='0',currentinventory='0' where (initinventory is null) and (currentinventory is null)";
		String sql6 = "update dt_sumplan su set su.realnumber = (select sum(sh.plannumber) from dt_sharedpart sh,dt_dataprocess d where d.jqcode=su.jqcode and d.bdcode=su.bdcode and d.qccode=su.qccode and d.dataprocess_id=sh.dataprocess_id) where exists (select sum(sh.plannumber) from dt_sharedpart sh,dt_dataprocess d where d.jqcode=su.jqcode and d.bdcode=su.bdcode and d.qccode=su.qccode and d.dataprocess_id=sh.dataprocess_id)";
		String sql8 = "update dt_sumplan su set su.realnumber = (select sum(sp.number) from sp_item sp where sp.armyid=su.jqcode and sp.itemid=su.qccode) where su.realnumber is null";
		System.out.println(sql);
		dt_plandao.addSumplan(sql1);
		dt_plandao.addSumplan(sql);
		dt_plandao.addSumplan(sqll);
		dt_plandao.addSumplan(sqlll);
		dt_plandao.addSumplan(sql2);
		dt_plandao.addSumplan(sql33);
		dt_plandao.addSumplan(sql4);
		dt_plandao.addSumplan(sql5);
		dt_plandao.addSumplan(sql6);
		dt_plandao.addSumplan(sql8);
	}
	//添加调拨记录，分自筹和供应
	@Override
	public void adminallotrecord(Integer recordnumber,String sharedpart_id,String jqcode,String bdcode,String qccode,String qcname,Integer realsupply,String create_people,String createtime,String receive_people,String fg,Integer sum_allot_number,String desbdcode) {
		// TODO Auto-generated method stub
		System.out.println(fg);
		if(fg.equals("部队")){
			String insertsql = "insert into dt_datarecordlist(selfplan_id,jqcode,bdcode,qccode,qcname,this_allot_number,plan_supply_number,create_people,createtime,receive_people,sum_allot_number) values('"+sharedpart_id+"','"+jqcode+"','"+bdcode+"','"+qccode+"','"+qcname+"','"+recordnumber+"','"+realsupply+"','"+create_people+"','"+createtime+"','"+receive_people+"','"+sum_allot_number+"')";
			dt_plandao.addSumplan(insertsql);
			System.out.println(insertsql);
		}else{
			String insertsql = "insert into dt_datarecordlist(supplyplan_id,jqcode,bdcode,qccode,qcname,this_allot_number,plan_supply_number,create_people,createtime,receive_people,sum_allot_number) values('"+sharedpart_id+"','"+jqcode+"','"+bdcode+"','"+qccode+"','"+qcname+"','"+recordnumber+"','"+realsupply+"','"+create_people+"','"+createtime+"','"+receive_people+"','"+sum_allot_number+"')";
			dt_plandao.addSumplan(insertsql);
			System.out.println(insertsql);
		}
	}
	
	@Override
	public void refreshstorehouse(String sharedpart_id, String desbdcode,String jqcode,String bdcode,String qccode,
			String qcname, Integer remain_store,Integer storehouse_remain_store) {
		// TODO Auto-generated method stub
		String sql = "update dt_storehouse set currentinventory="+storehouse_remain_store+" where jqcode='"+jqcode+"' and bdcode='"+bdcode+"' and qccode='"+qccode+"' and qcname='"+qcname+"'";
		String sql1 = "update dt_sumplan set currentinventory="+remain_store+" where jqcode='"+jqcode+"' and bdcode='"+bdcode+"' and qccode='"+qccode+"' and qcname='"+qcname+"'";
		dt_plandao.addSumplan(sql);
		dt_plandao.addSumplan(sql1);
		System.out.println(sql);
	}
	//供应计划修改
	@Override
	public void adminrealsupplyedit(String bdcode,String qccode,String qcname,String fg,Integer realsupply,String comments) {
		// TODO Auto-generated method stub
		String sql = "update dt_sumplan set realsupply="+realsupply+" where bdcode='"+bdcode+"' and qccode='"+qccode+"' and qcname='"+qcname+"'";
		dt_plandao.addSumplan(sql);
		System.out.println(sql);
	}
	@Override
	public void adminselfsupplyplanedit(String jqcode, String bdcode,String qccode,
			String qcname, String fg, Integer realnumber, String comments) {
		// TODO Auto-generated method stub
		String sql = "update dt_sumplan set realnumber="+realnumber+" where jqcode='"+jqcode+"' and bdcode='"+bdcode+"' and qccode='"+qccode+"' and qcname='"+qcname+"'";
		dt_plandao.addSumplan(sql);
		System.out.println(sql);
	}
}
