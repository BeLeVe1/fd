package com.hd.microblog.web.controller.admin;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.text.DecimalFormat;
import java.util.ArrayList;
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

import com.hd.microblog.model.dt_amount;
import com.hd.microblog.model.dt_analysis;
import com.hd.microblog.model.dt_sharedpart;
import com.hd.microblog.service.dt_adminService;
import com.hd.microblog.service.dt_amountService;
import com.hd.microblog.service.dt_dataprocessService;
import com.hd.microblog.service.dt_planService;
import com.hd.microblog.service.dt_sharedpartService;
import com.hd.microblog.util.createxls;




@Controller
public class AdminamountController {
	 
	@Autowired
	@Qualifier("dt_adminService")
	private dt_adminService dt_adminservice;
	@Autowired
	@Qualifier("dt_amountService")
	private dt_amountService dt_amountservice;
	@Autowired
	@Qualifier("dt_dataprocessService")
	private dt_dataprocessService dt_dataprocessservice;
	
	//金额表
	@RequestMapping("/adminamountlist")
	public String adminamountlist(HttpServletRequest request, HttpServletResponse resp) 
			throws IOException {
		return "admin/amountlist";
	}
	//金额表---军区
	@RequestMapping("/adminamountjqlist")
	public String adminamountjqlist(HttpServletRequest request, HttpServletResponse resp) 
			throws IOException {
		return "admin/amountjqlist";
	}
	//金额表---总部
	@RequestMapping("/adminamountzblist")
	public String adminamountzblist(HttpServletRequest request, HttpServletResponse resp) 
			throws IOException {
		return "admin/amountzblist";
	}
	//金额表---部队
	@RequestMapping("/adminamountbdlist")
	public String adminamountbdlist(HttpServletRequest request, HttpServletResponse resp) 
			throws IOException {
		return "admin/amountbdlist";
	}
	//金额表
	@RequestMapping(value = "/adminamountlistajax", method = { RequestMethod.POST }, produces = "application/json; charset=utf-8")
	@ResponseBody
	private String adminamountlistajax(HttpServletRequest request, Model model, String page, String rows ,Integer draw, 
			String zbcode,String zbname,String sort,String fg) throws IOException {
		
		adminamountstatistics(fg);
		
		Integer start = Integer.valueOf(request.getParameter("start"));  
	    String length = request.getParameter("length");
		int number = Integer.valueOf(length);
		List items = dt_amountservice.adminfindamountlist(zbcode,zbname,sort,start,number);
		List count = dt_amountservice.adminfindamountlistcount(zbcode,zbname);
		int countnumber = 0;
		if (count != null && count.size() != 0) {
			Map map = (Map) count.get(0);
			countnumber = Integer.valueOf(String.valueOf(map.get("count")));
		}
		List returnlist  = new ArrayList();
		for(int i=0;i<items.size();i++){
			Map map = (Map)items.get(i);
			
			returnlist.add(map);
		}
		
		JSONObject jobj = new JSONObject();
		
		jobj.accumulate("draw", draw);
		jobj.accumulate("recordsFiltered", countnumber);
		jobj.accumulate("recordsTotal", countnumber);
		jobj.accumulate("data", returnlist);
		return jobj.toString();
	}
	//Excel生成
	@RequestMapping(value = "/adminamountExcel",produces = "application/json; charset=utf-8")
	@ResponseBody
	private String adminamountExcel(HttpServletRequest request,HttpServletResponse resp) throws IOException {
		HttpSession session = request.getSession();
		resp.setHeader("Access-Control-Allow-Origin", "*");
		resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
		JSONObject json = new JSONObject();
		try{
			//生成xls表头
			List<String> header = new ArrayList<String>(); // 第一行数据
			List<List<String>> body = new ArrayList<List<String>>();
			header.add("装备代码");
		    header.add("装备名称");
		    header.add("装备花费金额");
		    List items = dt_amountservice.adminfindamountlist();
			for(int i=0;i<items.size();i++){
				Map map = (Map)items.get(i);
				//添加xls信息
				List<String> data = new ArrayList<String>();
				data.add(String.valueOf(map.get("zbcode")));
				data.add(String.valueOf(map.get("zbname")));
				data.add(String.valueOf(map.get("money")));
		    	body.add(data);
			}
			//xls输出
			String loadpath = request.getSession().getServletContext().getRealPath("/") + "..//upload" + File.separator;
		    //新建文件路径
		    File file2 = new File(loadpath);
			if (!file2.exists()) {
				file2.mkdir();
			}
			try(OutputStream out = new FileOutputStream(loadpath+"/"+"装备金额确认.xls")){
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
	//统计
	private void adminamountstatistics(String fg) throws IOException {
		JSONObject json = new JSONObject();
		List amountlist = dt_amountservice.adminfindamountlistAll();
		for(int i=0;i<amountlist.size();i++) {
			Map map = (Map)amountlist.get(i);
			dt_amountservice.delete(Integer.valueOf(String.valueOf(map.get("amount_id"))));
		}
		
		List list = dt_dataprocessservice.adminfinddataprocessgroup(fg);
		for(int i=0;i<list.size();i++){
			Map map = (Map)list.get(i);
			dt_amount amount = new dt_amount();
			amount.setZbcode(String.valueOf(map.get("zbcode")));
			amount.setZbname(String.valueOf(map.get("zbcode"))+"装备");
			amount.setMoney(Double.valueOf(String.valueOf(map.get("zbmoney"))));
			dt_amountservice.saveOrUpdate(amount);
			
			System.out.println("==="+i);
		}
	}	
}






