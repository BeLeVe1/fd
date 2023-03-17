package com.hd.microblog.web.controller.admin;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import net.sf.json.JSONObject;

import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import com.hd.microblog.model.dt_admin;
import com.hd.microblog.model.dt_dataprocess;
import com.hd.microblog.model.dt_datarecord;
import com.hd.microblog.model.dt_plan;
import com.hd.microblog.model.dt_sharedpart;
import com.hd.microblog.model.dt_allotrecord;
import com.hd.microblog.model.dt_storehouse;

import com.hd.microblog.service.dt_adminService;
import com.hd.microblog.service.dt_dataprocessService;
import com.hd.microblog.service.dt_datarecordService;
import com.hd.microblog.service.dt_planService;
import com.hd.microblog.service.dt_sharedpartService;
import com.hd.microblog.service.dt_allotrecordService;
import com.hd.microblog.util.createxls;
import com.hd.common.util.MD5;


@Controller
public class AdminallotrecordController {
	
	@Autowired
	@Qualifier("dt_allotrecordService")
	private dt_allotrecordService dt_allotrecordservice;
	
	@Autowired
	@Qualifier("dt_sharedpartService")
	private dt_sharedpartService dt_sharedpartservice;
	
	//制定调拨记录表
	@RequestMapping("/adminallotrecord")
	public String adminallotrecord(HttpServletRequest request, HttpServletResponse resp) 
			throws IOException {
		return "admin/allotrecord";
	}
	//制定年度供应计划表
	@RequestMapping(value = "/adminallotrecordajax", method = { RequestMethod.POST }, produces = "application/json; charset=utf-8")
	@ResponseBody
	private String adminallotrecordajax(HttpServletRequest request, Model model, String page, String rows ,Integer draw, 
			Integer allot_id,Integer supplyplan_id,Integer selfplan_id,String jqcode,String bdcode,String qccode,String qcname,Integer this_allot_number,Integer plan_supply_number,Integer sum_allot_number,
			String from_store,String to_store,String create_people,Integer createtime,String receive_people,String total_price, String customer_name, String checker,
			String contract, String reviser, String modification_date,
			String preparation_time, String Audit_time,String sort) throws IOException {
		System.out.println("lueluiele:");
		Integer start = Integer.valueOf(request.getParameter("start"));
		System.out.println(start);
		String length = request.getParameter("length");
		System.out.println(length);
		int number = Integer.valueOf(length);
		List items = dt_allotrecordservice.adminfindsupplyplanlist(allot_id,supplyplan_id,selfplan_id,jqcode,bdcode,qccode,qcname,this_allot_number,plan_supply_number,sum_allot_number,
				from_store,to_store,create_people,createtime,receive_people,total_price,customer_name,checker,contract,reviser,modification_date,preparation_time,Audit_time,sort,start,number);
		List count = dt_allotrecordservice.adminfindsupplyplanlistcount(allot_id,supplyplan_id,selfplan_id, jqcode, bdcode, qccode, qcname, this_allot_number, plan_supply_number, sum_allot_number,
				 from_store, to_store, create_people, createtime, receive_people, total_price,  customer_name,  checker,
				 contract,  reviser,  modification_date,
				 preparation_time,  Audit_time);
		System.out.println("items:");
		System.out.println(items);
		int countnumber = 0;
		if (count != null && count.size() != 0) {
			Map map = (Map) count.get(0);
			countnumber = Integer.valueOf(String.valueOf(map.get("count")));
		}
		List returnlist  = new ArrayList();
		
		for(int i=0;i<items.size();i++){
			Map map = (Map)items.get(i);
			map.put("czflag", 1);
			returnlist.add(map);
		}
		JSONObject jobj = new JSONObject();
				
		jobj.accumulate("draw", draw);
		jobj.accumulate("recordsFiltered", countnumber);
		jobj.accumulate("recordsTotal", countnumber);
		jobj.accumulate("data", returnlist);
		
		System.out.println("json为=");
		System.out.println(jobj);
		return jobj.toString();
	}
	
	@RequestMapping("/adminallotrecordchange")
	public String adminapplyplanedit(HttpServletRequest request, HttpServletResponse resp,Integer allot_id,Integer sum_allot_number,String jqcode,String bdcode,String from_store,
			String qccode,String qcname,String this_allot_number) 
			throws IOException {
		
		request.setAttribute("allot_id", allot_id);
		request.setAttribute("sum_allot_number", sum_allot_number);
		request.setAttribute("old_allot_number", this_allot_number);
		request.setAttribute("jqcode", jqcode);
		request.setAttribute("bdcode", bdcode);
		request.setAttribute("from_store", from_store);
		request.setAttribute("qccode", qccode);
		request.setAttribute("qcname", qcname);
		request.setAttribute("this_allot_number", this_allot_number);


		return "admin/allotrecordchange";
	}
	
	@RequestMapping(value = "/adminallotrecordchangeajax",produces = "application/json; charset=utf-8")
	@ResponseBody
	private String adminallotrecordchangeajax(HttpServletRequest request,HttpServletResponse resp,Integer allot_id,
			Integer sum_allot_number,Integer old_allot_number,String jqcode,String bdcode,String from_store,
			String qccode,String qcname,Integer this_allot_number) throws IOException {
		
		HttpSession session = request.getSession();
		resp.setHeader("Access-Control-Allow-Origin", "*");
		resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
		JSONObject json = new JSONObject();
		DecimalFormat df = new DecimalFormat("#");
		
		//不取值，直接更新数值
		try{
			//更新调拨记录表
			dt_allotrecordservice.refreshallotrecord(allot_id,jqcode,bdcode,from_store,qccode,qcname,this_allot_number,old_allot_number,sum_allot_number);
			//更新当前库存
			//dt_allotrecordservice.refreshstorehouse(jqcode,from_store,qccode,qcname,this_allot_number,old_allot_number);
			json.put("code", "100");
			json.put("info", "更新成功");
		}catch(Exception e){
			e.printStackTrace();
			json.put("code", "400");
			json.put("info", "系统错误");
		}
		return json.toString();
	}
}
