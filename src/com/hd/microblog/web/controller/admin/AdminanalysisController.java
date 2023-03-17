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

import com.hd.microblog.model.dt_analysis;
import com.hd.microblog.model.dt_dataprocess;
import com.hd.microblog.model.dt_prediction;
import com.hd.microblog.model.dt_sharedpart;
import com.hd.microblog.service.dt_adminService;
import com.hd.microblog.service.dt_analysisService;
import com.hd.microblog.service.dt_dataprocessService;
import com.hd.microblog.service.dt_predictionService;
import com.hd.microblog.service.dt_sharedpartService;
import com.hd.microblog.util.createxls;




@Controller
public class AdminanalysisController {
	 
	@Autowired
	@Qualifier("dt_analysisService")
	private dt_analysisService dt_analysisservice;
	@Autowired
	@Qualifier("dt_dataprocessService")
	private dt_dataprocessService dt_dataprocessservice;
	@Autowired
	@Qualifier("dt_sharedpartService")
	private dt_sharedpartService dt_sharedpartservice;
	@Autowired
	@Qualifier("dt_predictionService")
	private dt_predictionService dt_predictionservice;
	
	//预测分析表
	@RequestMapping("/adminanalysislist")
	public String adminanalysislist(HttpServletRequest request, HttpServletResponse resp) 
			throws IOException {
		return "admin/analysislist";
	}
	//预测分析表
	@RequestMapping(value = "/adminanalysislistajax", method = { RequestMethod.POST }, produces = "application/json; charset=utf-8")
	@ResponseBody
	private String adminanalysislistajax(HttpServletRequest request, Model model, String page, String rows ,Integer draw, 
			String jqcode,String bdcode,String zbcode,String qccode,String qcname,String fg,String sort) throws IOException {
		fg="";
		Integer start = Integer.valueOf(request.getParameter("start"));
	    String length = request.getParameter("length");
		int number = Integer.valueOf(length);
		List items = dt_analysisservice.adminfindanalysislist(jqcode,bdcode,zbcode,qccode,qcname,fg,sort,start,number);
		List count = dt_analysisservice.adminfindanalysislistcount(jqcode,bdcode,zbcode,qccode,qcname,fg);
		int countnumber = 0;
		if (count != null && count.size() != 0) {
			Map map = (Map) count.get(0);
			countnumber = Integer.valueOf(String.valueOf(map.get("count")));
		}
		List returnlist  = new ArrayList();
		for(int i=0;i<items.size();i++){
			Map map = (Map)items.get(i);
			if(Integer.valueOf(String.valueOf(map.get("ycff")))==1) {
				map.put("ycffname", "简单移动平均法");
			}else if(Integer.valueOf(String.valueOf(map.get("ycff")))==2) {
				map.put("ycffname", "指数平滑法");
			}else if(Integer.valueOf(String.valueOf(map.get("ycff")))==3) {
				map.put("ycffname", "线性回归法");
			}else if(Integer.valueOf(String.valueOf(map.get("ycff")))==4) {
				map.put("ycffname", "误差平方和倒数组合预测");
			}
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
	@RequestMapping(value = "/adminanalysisExcel",produces = "application/json; charset=utf-8")
	@ResponseBody
	private String adminanalysisExcel(HttpServletRequest request,HttpServletResponse resp) throws IOException {
		HttpSession session = request.getSession();
		resp.setHeader("Access-Control-Allow-Origin", "*");
		resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
		JSONObject json = new JSONObject();
		try{
			//生成xls表头
			List<String> header = new ArrayList<String>(); // 第一行数据
			List<List<String>> body = new ArrayList<List<String>>();
			header.add("军区编号");
		    header.add("部队编号");
			header.add("装备代码");
		    header.add("器材代码");
		    header.add("器材名称");
		    header.add("年份1");
		    header.add("年份2");
		    header.add("年份3");
		    header.add("年份4");
		    header.add("年份5");
		    header.add("年份6");
		    header.add("年份7");
		    header.add("年份8");
		    header.add("年份9");
		    header.add("年份10");
		    header.add("预测方法");
		    header.add("预测值");
		    header.add("方差");
		    
		    List items = dt_analysisservice.adminfindanalysislist();
			for(int i=0;i<items.size();i++){
				Map map = (Map)items.get(i);
				if(Integer.valueOf(String.valueOf(map.get("ycff")))==1) {
					map.put("ycffname", "简单移动平均法");
				}else if(Integer.valueOf(String.valueOf(map.get("ycff")))==2) {
					map.put("ycffname", "指数平滑法");
				}else if(Integer.valueOf(String.valueOf(map.get("ycff")))==3) {
					map.put("ycffname", "线性回归法");
				}else if(Integer.valueOf(String.valueOf(map.get("ycff")))==4) {
					map.put("ycffname", "误差平方和倒数组合预测");
				}
				//添加xls信息
				List<String> data = new ArrayList<String>();
				data.add(String.valueOf(map.get("jqcode")));
				data.add(String.valueOf(map.get("bdcode")));
				data.add(String.valueOf(map.get("zbcode")));
				data.add(String.valueOf(map.get("qccode")));
				data.add(String.valueOf(map.get("qcname")));
				data.add(String.valueOf(map.get("age1")));
				data.add(String.valueOf(map.get("age2")));
				data.add(String.valueOf(map.get("age3")));
				data.add(String.valueOf(map.get("age4")));
				data.add(String.valueOf(map.get("age5")));
				data.add(String.valueOf(map.get("age6")));
				data.add(String.valueOf(map.get("age7")));
				data.add(String.valueOf(map.get("age8")));
				data.add(String.valueOf(map.get("age9")));
				data.add(String.valueOf(map.get("age10")));
				data.add(String.valueOf(map.get("ycffname")));
				data.add(String.valueOf(map.get("ycz11")));
				data.add(String.valueOf(map.get("fx11")));
		    	body.add(data);
		    	
			}
			//xls输出
			String loadpath = request.getSession().getServletContext().getRealPath("/") + "..//upload" + File.separator;
		    //新建文件路径
		    File file2 = new File(loadpath);
			if (!file2.exists()) {
				file2.mkdir();
			}
			try(OutputStream out = new FileOutputStream(loadpath+"/"+"预测分析.xls")){
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
	//折线图ajax
	@RequestMapping(value = "/zhexiantuajax", produces = "application/json; charset=utf-8")
	@ResponseBody
	public String zhexiantuajax(HttpServletRequest request, HttpServletResponse resp,Integer dataprocess_id) throws IOException {
		HttpSession session = request.getSession();
		resp.setHeader("Access-Control-Allow-Origin", "*");
		resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
		JSONObject json = new JSONObject();
		DecimalFormat df = new DecimalFormat("#");
		try {
			System.out.println(dataprocess_id);
			
			dt_dataprocess dataprocess = dt_dataprocessservice.get(dataprocess_id);
			//真实值
			List zszlist  = new ArrayList();
			zszlist.add(dataprocess.getAge1());
			zszlist.add(dataprocess.getAge2());
			zszlist.add(dataprocess.getAge3());
			zszlist.add(dataprocess.getAge4());
			zszlist.add(dataprocess.getAge5());
			zszlist.add(dataprocess.getAge6());
			zszlist.add(dataprocess.getAge7());
			zszlist.add(dataprocess.getAge8());
			zszlist.add(dataprocess.getAge9());
			zszlist.add(dataprocess.getAge10());
			zszlist.add(0);
			zszlist.add(0);
			System.out.println("====1"+zszlist);
			//移动平均法
			List ydlist = dt_predictionservice.adminfindpredictionfordidandtype(dataprocess_id,1);
			Map ydmap = (Map)ydlist.get(0);
			List ydpjlist  = new ArrayList();
			ydpjlist.add(Double.valueOf(String.valueOf(ydmap.get("ycz1"))));
			ydpjlist.add(Double.valueOf(String.valueOf(ydmap.get("ycz2"))));
			ydpjlist.add(Double.valueOf(String.valueOf(ydmap.get("ycz3"))));
			ydpjlist.add(Double.valueOf(String.valueOf(ydmap.get("ycz4"))));
			ydpjlist.add(Double.valueOf(String.valueOf(ydmap.get("ycz5"))));
			ydpjlist.add(Double.valueOf(String.valueOf(ydmap.get("ycz6"))));
			ydpjlist.add(Double.valueOf(String.valueOf(ydmap.get("ycz7"))));
			ydpjlist.add(Double.valueOf(String.valueOf(ydmap.get("ycz8"))));
			ydpjlist.add(Double.valueOf(String.valueOf(ydmap.get("ycz9"))));
			ydpjlist.add(Double.valueOf(String.valueOf(ydmap.get("ycz10"))));
			ydpjlist.add(Double.valueOf(String.valueOf(ydmap.get("ycz11"))));
			ydpjlist.add(Double.valueOf(String.valueOf(ydmap.get("ycz12"))));
			System.out.println("====2"+ydpjlist);
			//指数平滑法
			List zslist = dt_predictionservice.adminfindpredictionfordidandtype(dataprocess_id,2);
			Map zsmap = (Map)zslist.get(0);
			List zsphlist  = new ArrayList();
			zsphlist.add(Double.valueOf(String.valueOf(zsmap.get("ycz1"))));
			zsphlist.add(Double.valueOf(String.valueOf(zsmap.get("ycz2"))));
			zsphlist.add(Double.valueOf(String.valueOf(zsmap.get("ycz3"))));
			zsphlist.add(Double.valueOf(String.valueOf(zsmap.get("ycz4"))));
			zsphlist.add(Double.valueOf(String.valueOf(zsmap.get("ycz5"))));
			zsphlist.add(Double.valueOf(String.valueOf(zsmap.get("ycz6"))));
			zsphlist.add(Double.valueOf(String.valueOf(zsmap.get("ycz7"))));
			zsphlist.add(Double.valueOf(String.valueOf(zsmap.get("ycz8"))));
			zsphlist.add(Double.valueOf(String.valueOf(zsmap.get("ycz9"))));
			zsphlist.add(Double.valueOf(String.valueOf(zsmap.get("ycz10"))));
			zsphlist.add(Double.valueOf(String.valueOf(zsmap.get("ycz11"))));
			zsphlist.add(Double.valueOf(String.valueOf(zsmap.get("ycz12"))));
			System.out.println("====3"+zsphlist);
			//线性回归法
			List xxlist = dt_predictionservice.adminfindpredictionfordidandtype(dataprocess_id,3);
			Map xxmap = (Map)xxlist.get(0);
			List xxhglist  = new ArrayList();
			xxhglist.add(Double.valueOf(String.valueOf(xxmap.get("ycz1"))));
			xxhglist.add(Double.valueOf(String.valueOf(xxmap.get("ycz2"))));
			xxhglist.add(Double.valueOf(String.valueOf(xxmap.get("ycz3"))));
			xxhglist.add(Double.valueOf(String.valueOf(xxmap.get("ycz4"))));
			xxhglist.add(Double.valueOf(String.valueOf(xxmap.get("ycz5"))));
			xxhglist.add(Double.valueOf(String.valueOf(xxmap.get("ycz6"))));
			xxhglist.add(Double.valueOf(String.valueOf(xxmap.get("ycz7"))));
			xxhglist.add(Double.valueOf(String.valueOf(xxmap.get("ycz8"))));
			xxhglist.add(Double.valueOf(String.valueOf(xxmap.get("ycz9"))));
			xxhglist.add(Double.valueOf(String.valueOf(xxmap.get("ycz10"))));
			xxhglist.add(Double.valueOf(String.valueOf(xxmap.get("ycz11"))));
			xxhglist.add(Double.valueOf(String.valueOf(xxmap.get("ycz12"))));
			System.out.println("====4"+xxhglist);
			//线性回归法
			List wclist = dt_predictionservice.adminfindpredictionfordidandtype(dataprocess_id,4);
			Map wcmap = (Map)wclist.get(0);
			List wcpflist  = new ArrayList();
			wcpflist.add(Double.valueOf(String.valueOf(wcmap.get("ycz1"))));
			wcpflist.add(Double.valueOf(String.valueOf(wcmap.get("ycz2"))));
			wcpflist.add(Double.valueOf(String.valueOf(wcmap.get("ycz3"))));
			wcpflist.add(Double.valueOf(String.valueOf(wcmap.get("ycz4"))));
			wcpflist.add(Double.valueOf(String.valueOf(wcmap.get("ycz5"))));
			wcpflist.add(Double.valueOf(String.valueOf(wcmap.get("ycz6"))));
			wcpflist.add(Double.valueOf(String.valueOf(wcmap.get("ycz7"))));
			wcpflist.add(Double.valueOf(String.valueOf(wcmap.get("ycz8"))));
			wcpflist.add(Double.valueOf(String.valueOf(wcmap.get("ycz9"))));
			wcpflist.add(Double.valueOf(String.valueOf(wcmap.get("ycz10"))));
			wcpflist.add(Double.valueOf(String.valueOf(wcmap.get("ycz11"))));
			wcpflist.add(Double.valueOf(String.valueOf(wcmap.get("ycz12"))));
			System.out.println("====5"+wcpflist);
			json.put("zszlist", zszlist);
			json.put("ydpjlist", ydpjlist);
			json.put("zsphlist", zsphlist);
			json.put("xxhglist", xxhglist);
			json.put("wcpflist", wcpflist);
			json.put("code", "100");
			json.put("rinfo", "查询成功");
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
			json.put("code", "400");
			json.put("rinfo", "系统错误");
		}
		return json.toString();
	}
}






