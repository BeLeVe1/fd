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

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import com.hd.microblog.model.dt_admin;
import com.hd.microblog.model.dt_allotrecord;
import com.hd.microblog.model.dt_dataprocess;
import com.hd.microblog.model.dt_datarecord;
import com.hd.microblog.model.dt_plan;
import com.hd.microblog.model.dt_sharedpart;
import com.hd.microblog.model.dt_storehouse;

import com.hd.microblog.service.dt_adminService;
import com.hd.microblog.service.dt_allotrecordService;
import com.hd.microblog.service.dt_dataprocessService;
import com.hd.microblog.service.dt_datarecordService;
import com.hd.microblog.service.dt_planService;
import com.hd.microblog.service.dt_sharedpartService;
import com.hd.microblog.service.dt_storehouseService;
import com.hd.microblog.util.createxls;




@Controller
public class AdminplanController {
	 
	@Autowired
	@Qualifier("dt_adminService")
	private dt_adminService dt_adminservice;
	@Autowired
	@Qualifier("dt_planService")
	private dt_planService dt_planservice;
	@Autowired
	@Qualifier("dt_datarecordService")
	private dt_datarecordService dt_datarecordservice;
	@Autowired
	@Qualifier("dt_sharedpartService")
	private dt_sharedpartService dt_sharedpartservice;
	@Autowired
	@Qualifier("dt_dataprocessService")
	private dt_dataprocessService dt_dataprocessservice;
	@Autowired
	@Qualifier("dt_storehouseService")
	private dt_storehouseService dt_storehouseservice;
	@Autowired
	@Qualifier("dt_allotrecordService")
	private dt_allotrecordService dt_allotrecordservice;
	
	//制定计划表--战区
	@RequestMapping("/adminplanjqlist")
	public String adminplanjqlist(HttpServletRequest request, HttpServletResponse resp) 
			throws IOException {
		return "admin/planjqlist";
	}
	//制定计划表--部队
	@RequestMapping("/adminplanbdlist")
	public String adminplanbdlist(HttpServletRequest request, HttpServletResponse resp) 
			throws IOException {
		return "admin/planbdlist";
	}
	//制定计划表--陆装
	@RequestMapping("/adminplanzblist")
	public String adminplanzblist(HttpServletRequest request, HttpServletResponse resp) 
			throws IOException {
		return "admin/planzblist";
	}
	//制定计划表--年度供应计划
		@RequestMapping("/adminannualsupplyplan")
		public String adminannualsupplyplan(HttpServletRequest request, HttpServletResponse resp) 
				throws IOException {
			return "admin/annualsupplyplan";
		}
	//制定计划表--器材自筹计划
		@RequestMapping("/adminselfsupplyplan")
		public String adminselfsupplyplan(HttpServletRequest request, HttpServletResponse resp) 
				throws IOException {
			return "admin/selfsupplyplan";
		}
	//制定计划表--年度申请计划计划
		@RequestMapping("/adminannualapplyplan")
		public String adminannualapplyplan(HttpServletRequest request, HttpServletResponse resp) 
				throws IOException {
			return "admin/annualapplyplan";
		}
		//制定年度供应计划表
		@RequestMapping(value = "/adminannualsupplyplanajax", method = { RequestMethod.POST }, produces = "application/json; charset=utf-8")
		@ResponseBody
		private String adminannualsupplyplanajax(HttpServletRequest request, Model model, String page, String rows ,Integer draw, 
				String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg,String sort) throws IOException {
			
			Integer start = Integer.valueOf(request.getParameter("start"));  
		    String length = request.getParameter("length");  
			int number = Integer.valueOf(length);
			List items = dt_planservice.adminfindsupplyplanlist(jqcode,bdcode,zbcode,qccode,qcname,fg,sort,start,number);
			List count = dt_planservice.adminfindsupplyplanlistcount(jqcode,bdcode,zbcode,qccode,qcname,fg);
			int countnumber = 0;
			if (count != null && count.size() != 0) {
				Map map = (Map) count.get(0);
				countnumber = Integer.valueOf(String.valueOf(map.get("count")));
			}
			String jqcode2="";
			String qccode2="";
			
			String bdcode2="";
			String qcname2="";
			List returnlist  = new ArrayList();
			for(int i=0;i<items.size();i++){
				Map map = (Map)items.get(i);
				if(!map.get("fg").equals("")){
				System.out.println(map);
					List list = dt_sharedpartservice.adminfindsharedpartlistsum3(Integer.valueOf(String.valueOf(map.get("jqcode"))),String.valueOf(map.get("bdcode")),String.valueOf(map.get("qccode")),String.valueOf(map.get("qcname")));
					System.out.println(list);
					Map map2 = (Map)list.get(0);
					System.out.println(bdcode2+qcname2);
					if(String.valueOf(map.get("qccode")).equals(qccode2)&&String.valueOf(map.get("qcname")).equals(qcname2)&&String.valueOf(map.get("bdcode")).equals(bdcode2)) {
						
						map.put("number", "——");
						map.put("lastnumber", "——");
						
						map.put("plannumber", map2.get("plannumber"));
						map.put("currentnumber", "——");
						map.put("realsupply", "——");
						map.put("predictionnumber", map2.get("predictionnumber"));
						map.put("comments", map.get("type"));
						map.put("czflag", 0);
					}else {						
						map.put("plannumber", map.get("plannumber"));
						map.put("number", map2.get("initinventory"));
						map.put("lastnumber", map.get("realnumber"));
						map.put("predictionnumber", map.get("predictionnumber"));
						map.put("currentnumber", map.get("currentinventory"));
						map.put("realsupply", map.get("realsupply"));
						map.put("comments", map.get("type"));
						map.put("czflag", 1);
						qcname2=String.valueOf(map.get("qcname"));
						bdcode2=String.valueOf(map.get("bdcode"));
						qccode2=String.valueOf(map.get("qccode"));
					}
					returnlist.add(map);
				}
			}
			
			JSONObject jobj = new JSONObject();
			
			jobj.accumulate("draw", draw);
			jobj.accumulate("recordsFiltered", countnumber);
			jobj.accumulate("recordsTotal", countnumber);
			jobj.accumulate("data", returnlist);
			return jobj.toString();
		}
	//制定自筹表
		@RequestMapping(value = "/adminselfsupplypplanajax", method = { RequestMethod.POST }, produces = "application/json; charset=utf-8")
		@ResponseBody
		private String adminselfsupplypplanajax(HttpServletRequest request, Model model, String page, String rows ,Integer draw, 
				String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg,String sort) throws IOException {
			
			Integer start = Integer.valueOf(request.getParameter("start"));
		    String length = request.getParameter("length");  
			int number = Integer.valueOf(length);
			List items = dt_planservice.adminfindplanlist(jqcode,bdcode,zbcode,qccode,qcname,fg,sort,start,number);
			List count = dt_planservice.adminfindplanlistcount3(jqcode,bdcode,zbcode,qccode,qcname,fg);
			int countnumber = 0;
			if (count != null && count.size() != 0) {
				Map map = (Map) count.get(0);
				countnumber = Integer.valueOf(String.valueOf(map.get("count")));
			}
			String jqcode2="";
			String qccode2="";
			
			String bdcode2="";
			String qcname2="";
			List returnlist  = new ArrayList();
			for(int i=0;i<items.size();i++){
				Map map = (Map)items.get(i);
				if(map.get("fg").equals("部队")){
					//List list = dt_sharedpartservice.adminfindsharedpartlistsum2(Integer.valueOf(String.valueOf(map.get("qccode"))));
					//List list = dt_sharedpartservice.adminfindsharedpartlistsum2(Integer.valueOf(String.valueOf(map.get("bdcode"))),String.valueOf(map.get("qcname")));
					//战区级别自筹计划的求和
					List list = dt_sharedpartservice.adminfindsharedpartlistsum4(Integer.valueOf(String.valueOf(map.get("jqcode"))),String.valueOf(map.get("bdcode")),String.valueOf(map.get("qccode")),String.valueOf(map.get("qcname")));
					Map map2 = (Map)list.get(0);
					System.out.println(bdcode2+qcname2);
					if(String.valueOf(map.get("qccode")).equals(qccode2)&&String.valueOf(map.get("qcname")).equals(qcname2)&&String.valueOf(map.get("jqcode")).equals(jqcode2)&&String.valueOf(map.get("bdcode")).equals(bdcode2)) {
						
						map.put("number", "——");
						map.put("lastnumber", "——");
						
						map.put("plannumber", map2.get("plannumber"));
						map.put("predictionnumber", map2.get("predictionnumber"));
						map.put("currentnumber", "——");
						map.put("comments", map.get("type"));
						map.put("czflag", 0);
					}else {						
						map.put("plannumber", map.get("plannumber"));
						map.put("number", map.get("initinventory"));
						map.put("currentnumber", map.get("currentinventory"));
						map.put("lastnumber", map.get("realnumber"));
						map.put("predictionnumber", map.get("predictionnumber"));
						map.put("comments", map.get("type"));
						if(map2.get("type").equals("可修件")){
							map.put("czflag", 1);
						}else{
							map.put("czflag", 1);
						}						
						qcname2=String.valueOf(map.get("qcname"));
						jqcode2=String.valueOf(map.get("jqcode"));
						bdcode2=String.valueOf(map.get("bdcode"));
						qccode2=String.valueOf(map.get("qccode"));
						//returnlist.add(map);
						//countnumber=countnumber+1;
					}
					returnlist.add(map);
				}
			}
			
			JSONObject jobj = new JSONObject();
			
			jobj.accumulate("draw", draw);
			jobj.accumulate("recordsFiltered", countnumber);
			jobj.accumulate("recordsTotal", countnumber);
			jobj.accumulate("data", returnlist);
			return jobj.toString();
		}
		//制定年度申请计划表
		@RequestMapping(value = "/adminannualapplypplanajax", method = { RequestMethod.POST }, produces = "application/json; charset=utf-8")
		@ResponseBody
		private String adminannualapplypplanajax(HttpServletRequest request, Model model, String page, String rows ,Integer draw, 
				String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg,String sort) throws IOException {
			
			Integer start = Integer.valueOf(request.getParameter("start"));  
		    String length = request.getParameter("length");  
			int number = Integer.valueOf(length);
			List items = dt_planservice.adminfindapplyplanlist(jqcode,bdcode,zbcode,qccode,qcname,fg,sort,start,number);
			List count = dt_planservice.adminfindapplyplanlistcount(jqcode,bdcode,zbcode,qccode,qcname,fg);
			int countnumber = 0;
			if (count != null && count.size() != 0) {
				Map map = (Map) count.get(0);
				countnumber = Integer.valueOf(String.valueOf(map.get("count")));
			}
			String jqcode2="";
			String qccode2="";
			String bdcode2="";
			String qcname2="";
			List returnlist  = new ArrayList();
			for(int i=0;i<items.size();i++){
				Map map = (Map)items.get(i);
				if(!map.get("fg").equals("部队")){
					//List list = dt_sharedpartservice.adminfindsharedpartlistsum2(Integer.valueOf(String.valueOf(map.get("qccode"))));
					List list = dt_sharedpartservice.adminfindsharedpartlistsum4(Integer.valueOf(String.valueOf(map.get("jqcode"))),String.valueOf(map.get("bdcode")),String.valueOf(map.get("qccode")),String.valueOf(map.get("qcname")));
					Map map2 = (Map)list.get(0);
					System.out.println(bdcode2+qcname2);
					if(String.valueOf(map.get("qccode")).equals(qccode2)&&String.valueOf(map.get("qcname")).equals(qcname2)&&String.valueOf(map.get("jqcode")).equals(jqcode2)&&String.valueOf(map.get("bdcode")).equals(bdcode2)) {
						
						map.put("number", "——");
						map.put("lastnumber", "——");
						map.put("currentnumber", "——");
						map.put("plannumber", map2.get("plannumber"));
						map.put("predictionnumber", map2.get("predictionnumber"));
						map.put("comments", map.get("type"));
						map.put("czflag", 0);
					}else {						
						map.put("plannumber", map.get("plannumber"));
						map.put("number", map.get("initinventory"));
						map.put("currentnumber", map.get("currentinventory"));
						map.put("lastnumber", map.get("realnumber"));
						map.put("predictionnumber", map.get("predictionnumber"));
						map.put("comments", map.get("type"));
						map.put("czflag", 1);
						qcname2=String.valueOf(map.get("qcname"));
						jqcode2=String.valueOf(map.get("jqcode"));
						bdcode2=String.valueOf(map.get("bdcode"));
						qccode2=String.valueOf(map.get("qccode"));
					}
					returnlist.add(map);
				}
			}
			
			JSONObject jobj = new JSONObject();
			
			jobj.accumulate("draw", draw);
			jobj.accumulate("recordsFiltered", countnumber);
			jobj.accumulate("recordsTotal", countnumber);
			jobj.accumulate("data", returnlist);
			return jobj.toString();
		}
	//制定计划表
	@RequestMapping(value = "/adminplanlistajax", method = { RequestMethod.POST }, produces = "application/json; charset=utf-8")
	@ResponseBody
	private String adminplanlistajax(HttpServletRequest request, Model model, String page, String rows ,Integer draw, 
			String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg,String sort) throws IOException {
		
		Integer start = Integer.valueOf(request.getParameter("start"));  
	    String length = request.getParameter("length");  
		int number = Integer.valueOf(length);
		List items = dt_planservice.adminfindplanlist(jqcode,bdcode,zbcode,qccode,qcname,fg,sort,start,number);
		List count = dt_planservice.adminfindplanlistcount(jqcode,bdcode,zbcode,qccode,qcname,fg);
		int countnumber = 0;
		if (count != null && count.size() != 0) {
			Map map = (Map) count.get(0);
			countnumber = Integer.valueOf(String.valueOf(map.get("count")));
		}
		String jqcode2="";
		String qccode2="";
		List returnlist  = new ArrayList();
		for(int i=0;i<items.size();i++){
			Map map = (Map)items.get(i);
			if(fg.equals("陆装")){
				List list = dt_sharedpartservice.adminfindsharedpartlistsum2(String.valueOf(map.get("qcname")));
				Map map2 = (Map)list.get(0);
				map.put("plannumber", map2.get("plannumber"));
				map.put("number", map2.get("number"));
				map.put("makingplansnumber", map2.get("makingplansnumber"));
				map.put("thistimeplansnumber", map2.get("thistimeplansnumber"));
				map.put("lastnumber", map2.get("lastnumber"));
				
				if(String.valueOf(map.get("qccode")).equals(qccode2)) {
					
					map.put("number", "——");
					map.put("makingplansnumber", "——");
					map.put("thistimeplansnumber", "——");
					map.put("lastnumber", "——");
					
					map.put("plannumber", "——");
					map.put("kyd", "——");
					map.put("czflag", 0);
					qccode2=String.valueOf(map.get("qccode"));
				}else {
					map.put("czflag", 1);
					qccode2=String.valueOf(map.get("qccode"));
				}
				returnlist.add(map);
			}else if(fg.equals("部队")) {
				map.put("czflag", 1);
				returnlist.add(map);
			}else {
				List list = dt_sharedpartservice.adminfindsharedpartlistsum2(Integer.valueOf(String.valueOf(map.get("jqcode"))),String.valueOf(map.get("qccode")));
				Map map2 = (Map)list.get(0);
				map.put("plannumber", map2.get("plannumber"));
				map.put("number", map2.get("number"));
				map.put("makingplansnumber", map2.get("makingplansnumber"));
				map.put("thistimeplansnumber", map2.get("thistimeplansnumber"));
				map.put("lastnumber", map2.get("lastnumber"));
				
				if(String.valueOf(map.get("jqcode")).equals(jqcode2)&&String.valueOf(map.get("qccode")).equals(qccode2)) {
					
					map.put("number", "——");
					map.put("makingplansnumber", "——");
					map.put("thistimeplansnumber", "——");
					map.put("lastnumber", "——");
					
					map.put("plannumber", "——");
					map.put("kyd", "——");
					map.put("czflag", 0);
					jqcode2=String.valueOf(map.get("jqcode"));
					qccode2=String.valueOf(map.get("qccode"));
				}else {
					map.put("czflag", 1);
					jqcode2=String.valueOf(map.get("jqcode"));
					qccode2=String.valueOf(map.get("qccode"));
				}
				returnlist.add(map);
			}
		}
		
		JSONObject jobj = new JSONObject();
		
		jobj.accumulate("draw", draw);
		jobj.accumulate("recordsFiltered", countnumber);
		jobj.accumulate("recordsTotal", countnumber);
		jobj.accumulate("data", returnlist);
		return jobj.toString();
	}
	//Excel生成--器材自筹计划
	@RequestMapping(value = "/adminplanjqExcel",produces = "application/json; charset=utf-8")
	@ResponseBody
	private String adminplanjqExcel(HttpServletRequest request,HttpServletResponse resp) throws IOException {
		HttpSession session = request.getSession();
		resp.setHeader("Access-Control-Allow-Origin", "*");
		resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
		JSONObject json = new JSONObject();
		try{
			String fg="部队";
			//生成xls表头
			List<String> header = new ArrayList<String>(); // 第一行数据
			List<List<String>> body = new ArrayList<List<String>>();
			header.add("战区编号");
			header.add("部队编号");
			header.add("装备代码");
			header.add("器材代码");
		    header.add("器材名称");
		    header.add("分工");
		    header.add("预测消耗数量");
		    header.add("计算需求数量");
		    header.add("期初库存");
		    header.add("当前库存");
		    header.add("计划自筹数量");
		    header.add("类型");
			String jqcode2="";
			String qccode2="";
			
			String bdcode2="";
			String qcname2="";
		    List items = dt_planservice.adminfindplanlist(fg);
		    for(int i=0;i<items.size();i++){
				Map map = (Map)items.get(i);
				if(map.get("fg").equals("部队")){
					//List list = dt_sharedpartservice.adminfindsharedpartlistsum2(Integer.valueOf(String.valueOf(map.get("qccode"))));
					//List list = dt_sharedpartservice.adminfindsharedpartlistsum2(Integer.valueOf(String.valueOf(map.get("bdcode"))),String.valueOf(map.get("qcname")));
					//战区级别自筹计划的求和
					List list = dt_sharedpartservice.adminfindsharedpartlistsum4(Integer.valueOf(String.valueOf(map.get("jqcode"))),String.valueOf(map.get("bdcode")),String.valueOf(map.get("qccode")),String.valueOf(map.get("qcname")));
					Map map2 = (Map)list.get(0);
					System.out.println(bdcode2+qcname2);
					if(String.valueOf(map.get("qccode")).equals(qccode2)&&String.valueOf(map.get("qcname")).equals(qcname2)&&String.valueOf(map.get("jqcode")).equals(jqcode2)&&String.valueOf(map.get("bdcode")).equals(bdcode2)) {
						
						map.put("number", "——");
						map.put("lastnumber", "——");
						
						map.put("plannumber", map2.get("plannumber"));
						map.put("predictionnumber", map2.get("predictionnumber"));
						map.put("currentnumber", "——");
						map.put("comments", map.get("type"));
						map.put("czflag", 0);
					}else {						
						map.put("plannumber", map.get("plannumber"));
						map.put("number", map.get("initinventory"));
						map.put("currentnumber", map.get("currentinventory"));
						map.put("lastnumber", map.get("realnumber"));
						map.put("predictionnumber", map.get("predictionnumber"));
						map.put("comments", map.get("type"));
						if(map2.get("type").equals("可修件")){
							map.put("czflag", 1);
						}else{
							map.put("czflag", 1);
						}						
						qcname2=String.valueOf(map.get("qcname"));
						jqcode2=String.valueOf(map.get("jqcode"));
						bdcode2=String.valueOf(map.get("bdcode"));
						qccode2=String.valueOf(map.get("qccode"));
						//returnlist.add(map);
						//countnumber=countnumber+1;
					}
				//添加xls信息
					List<String> data = new ArrayList<String>();
					data.add(String.valueOf(map.get("jqcode")));
					data.add(String.valueOf(map.get("bdcode")));
					data.add(String.valueOf(map.get("zbcode")));
					data.add(String.valueOf(map.get("qccode")));
					data.add(String.valueOf(map.get("qcname")));
					data.add(String.valueOf(map.get("fg")));
					data.add(String.valueOf(map.get("predictionnumber")));
					data.add(String.valueOf(map.get("plannumber")));
					data.add(String.valueOf(map.get("number")));
					data.add(String.valueOf(map.get("currentnumber")));
					data.add(String.valueOf(map.get("lastnumber")));
					data.add(String.valueOf(map.get("comments")));
				
					body.add(data);
				}
			}
			//xls输出
			String loadpath = request.getSession().getServletContext().getRealPath("/") + "..//upload" + File.separator;
			//String loadpath = request.getSession().getServletContext().getRealPath("/") + File.separator;
		    //新建文件路径
		    File file2 = new File(loadpath);
		    //file2.createNewFile();
			if (!file2.exists()) {
				file2.mkdir();
			}
			try(OutputStream out = new FileOutputStream(loadpath+"/"+"器材自筹计划-部队.xls")){
				createxls.generateExcel("Sheet1", header, body, out);
			} catch (Exception e) {
				e.printStackTrace();
			}
			json.put("code", "100");
			json.put("info", "生成成功");
		}catch(Exception e){
			e.printStackTrace();
			json.put("code", "400");
			json.put("info", "系统错误");
		}
		return json.toString();
	}
	//Excel生成--年度供应计划
	@RequestMapping(value = "/adminplanbdExcel",produces = "application/json; charset=utf-8")
	@ResponseBody
	private String adminplanbdExcel(HttpServletRequest request,HttpServletResponse resp) throws IOException {
		HttpSession session = request.getSession();
		resp.setHeader("Access-Control-Allow-Origin", "*");
		resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
		JSONObject json = new JSONObject();
		try{
			String fg="部队";
			//生成xls表头
			List<String> header = new ArrayList<String>(); // 第一行数据
			List<List<String>> body = new ArrayList<List<String>>();
			header.add("战区编号");
			header.add("部队编号");
			header.add("装备代码");
			header.add("器材代码");
		    header.add("器材名称");
//		    header.add("单位");
//		    header.add("单价");
//		    header.add("单装用数");
		    header.add("分工");
		    header.add("预测消耗数量");
		    header.add("计划申请数量");
		    header.add("计划申请/自筹数量");
		    header.add("期初库存");
		    header.add("当前库存");
		    header.add("计划供应数量");
		    header.add("类型");
//		    header.add("本次制定数");
//		    header.add("剩余计划数");
		    String jqcode2="";
			String qccode2="";
			
			String bdcode2="";
			String qcname2="";
		    List items = dt_planservice.adminfindplanlist(fg);
		    for(int i=0;i<items.size();i++){
				Map map = (Map)items.get(i);
				if(!map.get("fg").equals("")){
				System.out.println(map);
					List list = dt_sharedpartservice.adminfindsharedpartlistsum3(Integer.valueOf(String.valueOf(map.get("jqcode"))),String.valueOf(map.get("bdcode")),String.valueOf(map.get("qccode")),String.valueOf(map.get("qcname")));
					System.out.println(list);
					Map map2 = (Map)list.get(0);
					System.out.println(bdcode2+qcname2);
					if(String.valueOf(map.get("qccode")).equals(qccode2)&&String.valueOf(map.get("qcname")).equals(qcname2)&&String.valueOf(map.get("bdcode")).equals(bdcode2)) {
						
						map.put("number", "——");
						map.put("lastnumber", "——");
						
						map.put("plannumber", map2.get("plannumber"));
						map.put("currentnumber", "——");
						map.put("realsupply", "——");
						map.put("predictionnumber", map2.get("predictionnumber"));
						map.put("comments", map.get("type"));
						map.put("czflag", 0);
					}else {						
						map.put("plannumber", map.get("plannumber"));
						map.put("number", map.get("initinventory"));
						map.put("lastnumber", map.get("realnumber"));
						map.put("predictionnumber", map.get("predictionnumber"));
						map.put("currentnumber", map.get("currentinventory"));
						map.put("realsupply", map.get("realsupply"));
						map.put("comments", map.get("type"));
						map.put("czflag", 1);
						qcname2=String.valueOf(map.get("qcname"));
						bdcode2=String.valueOf(map.get("bdcode"));
						qccode2=String.valueOf(map.get("qccode"));
					}
				//添加xls信息
				List<String> data = new ArrayList<String>();
				data.add(String.valueOf(map.get("jqcode")));
				data.add(String.valueOf(map.get("bdcode")));
				data.add(String.valueOf(map.get("zbcode")));
				data.add(String.valueOf(map.get("qccode")));
				data.add(String.valueOf(map.get("qcname")));
//				data.add(String.valueOf(map.get("unit")));
//				data.add(String.valueOf(map.get("unitprice")));
//				data.add(String.valueOf(map.get("dzys")));
				data.add(String.valueOf(map.get("fg")));
				data.add(String.valueOf(map.get("predictionnumber")));
				data.add(String.valueOf(map.get("plannumber")));
				data.add(String.valueOf(map.get("lastnumber")));				
				data.add(String.valueOf(map.get("number")));
				data.add(String.valueOf(map.get("currentnumber")));
				data.add(String.valueOf(map.get("realnumber")));
				data.add(String.valueOf(map.get("type")));
				
		    	body.add(data);
				}
			}
			//xls输出
			String loadpath = request.getSession().getServletContext().getRealPath("/") + "..//upload" + File.separator;
		    //新建文件路径
		    File file2 = new File(loadpath);
			if (!file2.exists()) {
				file2.mkdir();
			}
			try(OutputStream out = new FileOutputStream(loadpath+"/"+"年度供应计划-部队.xls")){
				createxls.generateExcel("Sheet1", header, body, out);
			} catch (Exception e) {
				e.printStackTrace();
			}
			json.put("code", "100");
			json.put("info", "生成成功");
		}catch(Exception e){
			e.printStackTrace();
			json.put("code", "400");
			json.put("info", "系统错误");
		}
		return json.toString();
	}	
	//Excel生成--年度申请计划
	@RequestMapping(value = "/adminplanzbExcel",produces = "application/json; charset=utf-8")
	@ResponseBody
	private String adminplanzbExcel(HttpServletRequest request,HttpServletResponse resp) throws IOException {
		HttpSession session = request.getSession();
		resp.setHeader("Access-Control-Allow-Origin", "*");
		resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
		JSONObject json = new JSONObject();
		try{
			String fg="部队";
			//生成xls表头
			List<String> header = new ArrayList<String>(); // 第一行数据
			List<List<String>> body = new ArrayList<List<String>>();
			header.add("战区编号");
			header.add("部队编号");
			header.add("装备代码");
			header.add("器材代码");
		    header.add("器材名称");
//		    header.add("单位");
//		    header.add("单价");
//		    header.add("单装用数");
		    header.add("分工");
		    header.add("预测消耗数量");
		    header.add("计算需求数量");
		    header.add("期初库存");
		    header.add("当前库存");
		    header.add("部队计划申请数量");
		    header.add("类型");
//		    header.add("本次制定数");
//		    header.add("剩余计划数");
		    String jqcode2="";
			String qccode2="";
			
			String bdcode2="";
			String qcname2="";
		    List items = dt_planservice.adminfindplanlist(fg);
		    for(int i=0;i<items.size();i++){
				Map map = (Map)items.get(i);
				if(!map.get("fg").equals("部队")){
					//List list = dt_sharedpartservice.adminfindsharedpartlistsum2(Integer.valueOf(String.valueOf(map.get("qccode"))));
					List list = dt_sharedpartservice.adminfindsharedpartlistsum4(Integer.valueOf(String.valueOf(map.get("jqcode"))),String.valueOf(map.get("bdcode")),String.valueOf(map.get("qccode")),String.valueOf(map.get("qcname")));
					Map map2 = (Map)list.get(0);
					System.out.println(bdcode2+qcname2);
					if(String.valueOf(map.get("qccode")).equals(qccode2)&&String.valueOf(map.get("qcname")).equals(qcname2)&&String.valueOf(map.get("jqcode")).equals(jqcode2)&&String.valueOf(map.get("bdcode")).equals(bdcode2)) {
						
						map.put("number", "——");
						map.put("lastnumber", "——");
						map.put("currentnumber", "——");
						map.put("plannumber", map2.get("plannumber"));
						map.put("predictionnumber", map2.get("predictionnumber"));
						map.put("comments", map.get("type"));
						map.put("czflag", 0);
					}else {						
						map.put("plannumber", map.get("plannumber"));
						map.put("number", map.get("initinventory"));
						map.put("currentnumber", map.get("currentinventory"));
						map.put("lastnumber", map.get("realnumber"));
						map.put("predictionnumber", map.get("predictionnumber"));
						map.put("comments", map.get("type"));
						map.put("czflag", 1);
						qcname2=String.valueOf(map.get("qcname"));
						jqcode2=String.valueOf(map.get("jqcode"));
						bdcode2=String.valueOf(map.get("bdcode"));
						qccode2=String.valueOf(map.get("qccode"));
					}
					//添加xls信息
					List<String> data = new ArrayList<String>();
					data.add(String.valueOf(map.get("jqcode")));
					data.add(String.valueOf(map.get("bdcode")));
					data.add(String.valueOf(map.get("zbcode")));
					data.add(String.valueOf(map.get("qccode")));
					data.add(String.valueOf(map.get("qcname")));
//				data.add(String.valueOf(map.get("unit")));
//				data.add(String.valueOf(map.get("unitprice")));
//				data.add(String.valueOf(map.get("dzys")));
					data.add(String.valueOf(map.get("fg")));
					data.add(String.valueOf(map.get("predictionnumber")));
					data.add(String.valueOf(map.get("plannumber")));
					data.add(String.valueOf(map.get("initinventory")));
					data.add(String.valueOf(map.get("currentinventory")));
					data.add(String.valueOf(map.get("realnumber")));
					data.add(String.valueOf(map.get("type")));
				
					body.add(data);
				}
			}
			//xls输出
			String loadpath = request.getSession().getServletContext().getRealPath("/") + "..//upload" + File.separator;
		    //新建文件路径
		    File file2 = new File(loadpath);
			if (!file2.exists()) {
				file2.mkdir();
			}
			try(OutputStream out = new FileOutputStream(loadpath+"/"+"年度申请计划-部队.xls")){
				createxls.generateExcel("Sheet1", header, body, out);
			} catch (Exception e) {
				e.printStackTrace();
			}
			json.put("code", "100");
			json.put("info", "生成成功");
		}catch(Exception e){
			e.printStackTrace();
			json.put("code", "400");
			json.put("info", "系统错误");
		}
		return json.toString();
	}	
	
	//Excel生成--调拨记录
	@RequestMapping(value = "/adminallotrecordExcel",produces = "application/json; charset=utf-8")
	@ResponseBody
	private String adminallotrecordExcel(HttpServletRequest request,HttpServletResponse resp) throws IOException {
		HttpSession session = request.getSession();
		resp.setHeader("Access-Control-Allow-Origin", "*");
		resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
		JSONObject json = new JSONObject();
		try{
			//生成xls表头
			List<String> header = new ArrayList<String>(); // 第一行数据
			List<List<String>> body = new ArrayList<List<String>>();
			header.add("供应计划号");
			header.add("自筹计划号");
			header.add("战区编号");
			header.add("部队编号");
//			header.add("调出仓库编号");
			header.add("器材编号");
		    header.add("器材名称");
			header.add("调拨数量");
		    header.add("计划供应量");
		    header.add("累计供应量");
		    header.add("计划人");
		    header.add("计划时间");
		    header.add("领用人");

		    List items = dt_allotrecordservice.adminfindsupplyplanlist();
			for(int i=0;i<items.size();i++){
				Map map = (Map)items.get(i);
				
				//添加xls信息

				List<String> data = new ArrayList<String>();
				data.add(String.valueOf(map.get("supplyplan_id")));
				data.add(String.valueOf(map.get("selfplan_id")));
				data.add(String.valueOf(map.get("jqcode")));
				data.add(String.valueOf(map.get("bdcode")));
//				data.add(String.valueOf(map.get("from_store")));
				data.add(String.valueOf(map.get("qccode")));
				data.add(String.valueOf(map.get("qcname")));
				data.add(String.valueOf(map.get("this_allot_number")));
				data.add(String.valueOf(map.get("plan_supply_number")));
				data.add(String.valueOf(map.get("sum_allot_number")));
				data.add(String.valueOf(map.get("create_people")));
				data.add(String.valueOf(map.get("createtime")));
				data.add(String.valueOf(map.get("receive_people")));

				body.add(data);
			}
		//xls输出
			String loadpath = request.getSession().getServletContext().getRealPath("/") + "..//upload" + File.separator;
		//新建文件路径
			File file2 = new File(loadpath);
			if (!file2.exists()) {
				file2.mkdir();
			}
			try(OutputStream out = new FileOutputStream(loadpath+"/"+"调拨记录-部队.xls")){
				createxls.generateExcel("Sheet1", header, body, out);
			} catch (Exception e) {
				e.printStackTrace();
			}
			json.put("code", "100");
			json.put("info", "生成成功");
		}catch(Exception e){
			e.printStackTrace();
			json.put("code", "400");
			json.put("info", "系统错误");
		}
		return json.toString();
	}	
		
	//制定计划记录添加
	@RequestMapping("/adminplanadd")
	public String admindatarecordadd(HttpServletRequest request, HttpServletResponse resp,
			Integer plan_id,Integer flag) 
			throws IOException {//flag 1陆装  2战区  3部队
		dt_plan plan = dt_planservice.get(plan_id);
		dt_dataprocess dataprocess = dt_dataprocessservice.get(plan.getDataprocess_id());
		request.setAttribute("plan", plan);
		request.setAttribute("dataprocess", dataprocess);
		request.setAttribute("flag", flag);
		return "admin/planadd";
	}
	@RequestMapping(value = "/adminplanaddajax", method = { RequestMethod.POST }, produces = "application/json; charset=utf-8")
	@ResponseBody
	private Map adminplanaddajax(HttpServletRequest request,Integer plan_id,Integer number,String planpeople,
			String people,String text,Integer flag) throws IOException {
		HttpSession session = request.getSession();
		Map map = new HashMap<String, String>();
		try{
			//获取登录用户信息
//			dt_admin admin = (dt_admin) session.getAttribute("admin");
			//计划叠加
			dt_plan plan = dt_planservice.get(plan_id);
			plan.setMakingplansnumber(plan.getMakingplansnumber()+number);
			plan.setThistimeplansnumber(number);
			dt_planservice.saveOrUpdate(plan);
			//查询数据处理表
			dt_dataprocess dataprocess = dt_dataprocessservice.get(plan.getDataprocess_id());
			//保存记录
			dt_datarecord datarecord = new dt_datarecord();
			datarecord.setDataprocess_id(plan_id);
			datarecord.setAdmin_id(1);
			datarecord.setFlag(flag);
			//flag 1陆装  2战区  3部队
			if(flag==1) {
				datarecord.setJhcode(dataprocess.getQccode()+String.valueOf(Integer.valueOf(String.valueOf(System.currentTimeMillis() / 1000))));
			}else if(flag==2) {
				datarecord.setJhcode(dataprocess.getJqcode()+dataprocess.getQccode()+String.valueOf(Integer.valueOf(String.valueOf(System.currentTimeMillis() / 1000))));
			}else if(flag==3) {
				datarecord.setJhcode(dataprocess.getBdcode()+dataprocess.getQccode()+String.valueOf(Integer.valueOf(String.valueOf(System.currentTimeMillis() / 1000))));
			}
			datarecord.setAge("年份10");
			datarecord.setNumber(number);
			datarecord.setPlanpeople(planpeople);
			datarecord.setPeople(people);
			datarecord.setText(text);
			datarecord.setCreatetime(Integer.valueOf(String.valueOf(System.currentTimeMillis() / 1000)));
			dt_datarecordservice.saveOrUpdate(datarecord);
			map.put("code", "100");
			map.put("info", "添加成功");
		}catch(Exception e){
			e.printStackTrace();
			map.put("code", "400");
			map.put("info", "添加失败");
		}
		return map;
	}
	//数据添加记录
	@RequestMapping("/admindatarecordlist")
	public String admindatarecordlist(HttpServletRequest request, HttpServletResponse resp,
			Integer plan_id,Integer flag) 
			throws IOException {
		request.setAttribute("flag", flag);
		request.setAttribute("plan_id", plan_id);
		return "admin/datarecordlist";
	}
	@RequestMapping(value = "/admindatarecordlistajax", method = { RequestMethod.POST }, produces = "application/json; charset=utf-8")
	@ResponseBody
	private String admindatarecordlistajax(HttpServletRequest request, Model model, String page, String rows ,Integer draw,
			Integer plan_id,Integer flag) throws IOException {
		
		dt_plan plan = dt_planservice.get(plan_id);
		
		Integer start = Integer.valueOf(request.getParameter("start"));  
	    String length = request.getParameter("length");  
		int number = Integer.valueOf(length);
		List items = dt_datarecordservice.adminfinddatarecordlist(start,number,plan.getDataprocess_id(),flag);
		List count = dt_datarecordservice.adminfinddatarecordlistcount(plan.getDataprocess_id(),flag);
		int countnumber = 0;
		if (count != null && count.size() != 0) {
			Map map = (Map) count.get(0);
			countnumber = Integer.valueOf(String.valueOf(map.get("count")));
		}
		List returnlist  = new ArrayList();
		for(int i=0;i<items.size();i++){
			Map map = (Map)items.get(i);
			//时间转换
			SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
			Long time = Long.valueOf(String.valueOf(map.get("createtime")))*1000;
			Date date = new Date(time);
			map.put("createtime",sdf.format(date));
			returnlist.add(map);
		}
		
		JSONObject jobj = new JSONObject();
		
		jobj.accumulate("draw", draw);
		jobj.accumulate("recordsFiltered", countnumber);
		jobj.accumulate("recordsTotal", countnumber);
		jobj.accumulate("data", returnlist);
		return jobj.toString();
	}
	
	//计划自筹数量修改
		@RequestMapping("/adminselfsupplyplanedit")
		public String adminselfsupplyplanedit(HttpServletRequest request, HttpServletResponse resp,Integer sharedpart_id,Integer plannumber,Integer number,Integer realnumber,Integer lastnumber,
				String jqcode,String bdcode,String qccode,String qcname,String comments) 
				throws IOException {
			dt_sharedpart sharedpart = dt_sharedpartservice.get(sharedpart_id);
			dt_storehouse storehouse = dt_storehouseservice.get(sharedpart_id);
			request.setAttribute("sharedpart_id", sharedpart_id);
			request.setAttribute("plannumber", plannumber);
			request.setAttribute("number", number);
			request.setAttribute("lastnumber", lastnumber);
			request.setAttribute("realnumber", realnumber);
			request.setAttribute("comments", comments);
			request.setAttribute("sharedpart", sharedpart);
			request.setAttribute("storehouse", storehouse);
			
			request.setAttribute("jqcode", jqcode);
			request.setAttribute("bdcode", bdcode);
			request.setAttribute("qccode", qccode);
			request.setAttribute("qcname", qcname);
			
			return "admin/selfsupplyplanedit";
		}
		
		//计划自筹数量修改
		@RequestMapping("/adminapplyplanedit")
		public String adminapplyplanedit(HttpServletRequest request, HttpServletResponse resp,Integer sharedpart_id,Integer plannumber,Integer number,Integer realnumber,Integer lastnumber,
				String jqcode,String bdcode,String qccode,String qcname,String comments) 
				throws IOException {
			dt_sharedpart sharedpart = dt_sharedpartservice.get(sharedpart_id);
			dt_storehouse storehouse = dt_storehouseservice.get(sharedpart_id);
			request.setAttribute("sharedpart_id", sharedpart_id);
			request.setAttribute("plannumber", plannumber);
			request.setAttribute("number", number);
			request.setAttribute("lastnumber", lastnumber);
			request.setAttribute("realnumber", realnumber);
			request.setAttribute("comments", comments);
			request.setAttribute("sharedpart", sharedpart);
			request.setAttribute("storehouse", storehouse);
			
			request.setAttribute("jqcode", jqcode);
			request.setAttribute("bdcode", bdcode);
			request.setAttribute("qccode", qccode);
			request.setAttribute("qcname", qcname);
	
			return "admin/applyplanedit";
		}
		
		@RequestMapping(value = "/adminselfsupplyplaneditajax",produces = "application/json; charset=utf-8")
		@ResponseBody
		private String adminselfsupplyplaneditajax(HttpServletRequest request,HttpServletResponse resp,Integer sharedpart_id,
				String jqcode,String bdcode,String qccode,String qcname,String fg,Integer realnumber,String comments) throws IOException {
			HttpSession session = request.getSession();
			resp.setHeader("Access-Control-Allow-Origin", "*");
			resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
			JSONObject json = new JSONObject();
			DecimalFormat df = new DecimalFormat("#");
			try{
				//dt_sharedpart sharedpart = dt_sharedpartservice.get(sharedpart_id);
//				if(comments.equals("消耗件")){
//					sharedpart.setRealnumber(realnumber);		
//					dt_sharedpartservice.saveOrUpdate(sharedpart);
//				}
				dt_planservice.adminselfsupplyplanedit(jqcode,bdcode,qccode,qcname,fg,realnumber,comments);
				json.put("code", "100");
				json.put("info", "更新成功");
			}catch(Exception e){
				e.printStackTrace();
				json.put("code", "400");
				json.put("info", "系统错误");
			}
			return json.toString();
		}
		//导入消耗件总表
		@RequestMapping("/adminsumplanlist")
		public String adminsumplanlist(HttpServletRequest request, HttpServletResponse resp) 
				throws IOException {
			return "admin/sumplanlist";
		}
		@RequestMapping(value = "/adminsumplanlistconsumeajax",produces = "application/json; charset=utf-8")
		@ResponseBody
		private String adminsumplanlistconsumeajax(HttpServletRequest request,HttpServletResponse resp,String fg) throws IOException {
			HttpSession session = request.getSession();
			resp.setHeader("Access-Control-Allow-Origin", "*");
			resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
			JSONObject json = new JSONObject();
			DecimalFormat df = new DecimalFormat("#");
			System.out.println(fg);
			try{
				dt_planservice.adminfindsumplanlist();
				json.put("code", "100");
				json.put("rinfo", "导入消耗件成功");
			}catch (Exception e) {
				e.printStackTrace();
				json.put("code", "400");
				json.put("rinfo", "系统错误");
			}
			
			return json.toString();
		}

		@RequestMapping(value = "/adminsumplanlistrepairajax",produces = "application/json; charset=utf-8")
		@ResponseBody
		private String adminsumplanlistrepairajax(HttpServletRequest request,HttpServletResponse resp,String fg) throws IOException {
			HttpSession session = request.getSession();
			resp.setHeader("Access-Control-Allow-Origin", "*");
			resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
			JSONObject json = new JSONObject();
			DecimalFormat df = new DecimalFormat("#");
			System.out.println(fg);
			try{
				json.put("code", "100");
				json.put("rinfo", "导入消耗件成功");
			}catch (Exception e) {
				e.printStackTrace();
				json.put("code", "400");
				json.put("rinfo", "系统错误");
			}
			return json.toString();
		}

		
		//调拨记录制定
		@RequestMapping("/adminallotrecordedit")
		public String adminallotrecordedit(HttpServletRequest request, HttpServletResponse resp,Integer sharedpart_id,Integer plannumber,Integer number,Integer lastnumber,String jqcode,String bdcode,String qccode,String qcname,String fg,Integer currentnumber,Integer realsupply,String createtime) 
				throws IOException {						
			request.setAttribute("sharedpart_id", sharedpart_id);
			request.setAttribute("jqcode", jqcode);
			request.setAttribute("bdcode", bdcode);
			request.setAttribute("qccode", qccode);
			request.setAttribute("qcname", qcname);
			request.setAttribute("plannumber", plannumber);
			request.setAttribute("number", number);
			request.setAttribute("lastnumber", lastnumber);
			request.setAttribute("fg", fg);
			request.setAttribute("currentnumber", currentnumber);
			request.setAttribute("realsupply", realsupply);
			SimpleDateFormat dff = new SimpleDateFormat("yyyy-MM-dd");// 设置日期格式
			createtime = dff.format(new Date());// 获取当前系统时间
			request.setAttribute("createtime", createtime);
			System.out.println(sharedpart_id+bdcode+qcname+plannumber+number+lastnumber+fg+currentnumber);
			return "admin/allotrecordedit";
		}
		
		@RequestMapping(value = "/adminallotrecordeditajax", produces = "application/json; charset=utf-8")
		@ResponseBody
		private String adminallotrecordeditajax(HttpServletRequest request, HttpServletResponse resp,
				String sharedpart_id, int recordnumber, String jqcode, String bdcode, String qccode, String qcname,
				Integer realsupply, Integer lastnumber, String desbdcode, Integer descurrentinventory,
				String create_people, String createtime, String receive_people, String fg, Integer currentnumber)
				throws IOException {
			HttpSession session = request.getSession();
			resp.setHeader("Access-Control-Allow-Origin", "*");
			resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
			JSONObject json = new JSONObject();
			System.out.println(currentnumber);
			DecimalFormat df = new DecimalFormat("#");
			if (currentnumber < recordnumber) {
				json.put("code", "400");
				json.put("info", "系统错误");
			} else {
				SimpleDateFormat dff = new SimpleDateFormat("yyyyMMddHHmmss");// 设置日期格式
				String dataline = dff.format(new Date());// 获取当前系统时间
				//Long timeLong = Long.parseLong(dataline)/10000;//超出上限的解决方法
				//sharedpart_id = timeLong.intValue();	
				sharedpart_id = dataline;
				// 取对应部队已调拨的最大累计调拨值
				List list = dt_allotrecordservice.sumallotrecord(bdcode, qccode, qcname);
				int sum_allot_number = 0;
				Integer remain_store = currentnumber - recordnumber;// 这个是用来更新dt_sumplan表的
				Integer storehouse_remain_store = currentnumber - recordnumber;// 这个用来更新dt_storehouse
				// String this_allot_number = list.get("this_allot_number");
				if (list != null && list.size() != 0) {
					Map map2 = (Map) list.get(0);
					sum_allot_number = (int) map2.get("sum_allot_number");
					System.out.println(sum_allot_number);
					sum_allot_number = sum_allot_number + recordnumber;
					System.out.println(sum_allot_number);
				} else {
					sum_allot_number = recordnumber;
				}
				try {
					// 插入调拨记录
					dt_planservice.adminallotrecord(recordnumber, sharedpart_id, jqcode, bdcode, qccode, qcname,
							realsupply, create_people, createtime, receive_people, fg, sum_allot_number, desbdcode);
					// 更新当前库存
					dt_planservice.refreshstorehouse(sharedpart_id, desbdcode, jqcode, bdcode, qccode, qcname,
							remain_store, storehouse_remain_store);
					json.put("code", "100");
					json.put("info", "更新成功");
				} catch (Exception e) {
					e.printStackTrace();
					json.put("code", "400");
					json.put("info", "系统错误");
				}
			}
			return json.toString();
		}
		
		//计划调拨数量修改
		@RequestMapping("/adminrealsupplyedit")
		public String adminrealsupplyedit(HttpServletRequest request, HttpServletResponse resp,String jqcode,String bdcode,String qccode,String qcname,String fg,Integer realsupply,String comments) 
				throws IOException {						
			request.setAttribute("jqcode", jqcode);
			request.setAttribute("bdcode", bdcode);
			request.setAttribute("qccode", qccode);
			request.setAttribute("qcname", qcname);
			request.setAttribute("fg", fg);
			request.setAttribute("realsupply", realsupply);
			request.setAttribute("comments", comments);
			System.out.println(bdcode+qcname+fg+realsupply);
			return "admin/realsupplyedit";
		}
		
		@RequestMapping(value = "/adminrealsupplyeditajax",produces = "application/json; charset=utf-8")
		@ResponseBody
		private String adminrealsupplyeditajax(HttpServletRequest request,HttpServletResponse resp,String jqcode,String bdcode,String qccode,String qcname,Integer realsupply,String fg,String comments) throws IOException {
			HttpSession session = request.getSession();
			resp.setHeader("Access-Control-Allow-Origin", "*");
			resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
			JSONObject json = new JSONObject();
			DecimalFormat df = new DecimalFormat("#");
			try{
				dt_planservice.adminrealsupplyedit(bdcode,qccode,qcname,fg,realsupply,comments);
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






