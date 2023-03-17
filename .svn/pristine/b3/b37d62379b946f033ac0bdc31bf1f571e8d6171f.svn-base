package com.hd.microblog.web.controller.admin;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.sql.SQLException;
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

import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import com.hd.common.util.MD5;
import com.hd.microblog.model.dt_admin;
import com.hd.microblog.service.dt_adminService;
import com.hd.microblog.service.dt_menuService;





@Controller
public class AdminindexController {
	
	@Autowired
	@Qualifier("dt_adminService")
	private dt_adminService dt_adminservice;
	@Autowired
	@Qualifier("dt_menuService")
	private dt_menuService dt_menuservice;
	
	//后台主页
	@RequestMapping("/adminindex")
	public String admin(HttpServletRequest request, HttpServletResponse resp) 
			throws IOException {
		HttpSession session = request.getSession();
		dt_admin admin = (dt_admin) session.getAttribute("admin");
		request.setAttribute("admin", admin);
		request.setAttribute("name", admin.getAccount());
		return "admin/index";
	}
	//密码修改
	@RequestMapping(value = "/adminupdatepasswordajax", method = { RequestMethod.POST }, produces = "application/json; charset=utf-8")
	@ResponseBody
	private Map adminupdatepasswordajax(HttpServletRequest request,String oldpassword,
			String newpassword
			) throws IOException {
		Map map = new HashMap<String, String>();
		HttpSession session = request.getSession();
		dt_admin admin1 = (dt_admin) session.getAttribute("admin");
		try{
			dt_admin admin = dt_adminservice.get(admin1.getAdmin_id());
			String oldpasswordmd5 = MD5.MD5Encode("y7<LF5H2qgfIx]AD{6Yg"+MD5.MD5Encode(oldpassword, "UTF-8"), "UTF-8");
			String newpasswordmd5 = MD5.MD5Encode("y7<LF5H2qgfIx]AD{6Yg"+MD5.MD5Encode(newpassword, "UTF-8"), "UTF-8");
			if(admin.getPassword().equals(oldpasswordmd5)){
				admin.setPassword(newpasswordmd5);
				dt_adminservice.saveOrUpdate(admin);
				map.put("code", "100");
				map.put("info", "修改成功");
			}else{
				map.put("code", "400");
				map.put("info", "原密码错误");
			}
		}catch(Exception e){
			e.printStackTrace();
			map.put("code", "400");
			map.put("info", "修改失败");
		}
		return map;
	}	
	//退出
	@RequestMapping("/adminquit")
	public String adminquit(HttpServletRequest request, HttpServletResponse resp) 
			throws IOException {
		HttpSession session = request.getSession();
		session.setAttribute("admin", null);
		return "admin/login";
	}
	//欢迎页面
//	@RequestMapping("/adminwelcome")
//	public String landlordwelcome(HttpServletRequest request, HttpServletResponse resp) 
//			throws IOException {
//		HttpSession session = request.getSession();
//		dt_admin admin = (dt_admin) session.getAttribute("admin");
//		return "admin/welcome";
//	}
	//主页
	@RequestMapping("/adminmain")
	public String landlordwelcome(HttpServletRequest request, HttpServletResponse resp) 
			throws IOException {
		HttpSession session = request.getSession();
		dt_admin admin = (dt_admin) session.getAttribute("admin");
		return "admin/main";
	}
	//导航列表
	@RequestMapping(value = "/adminmenulistajax", method = { RequestMethod.GET }, produces = "application/json; charset=utf-8")
	@ResponseBody
	private Map adminmenulistajax(HttpServletRequest request) throws IOException {
		Map map = new HashMap<String, String>();
		try{
			List list = dt_menuservice.adminfindmenulist();
			List returnlist  = new ArrayList();
			for(int i=0;i<list.size();i++){
				Map map2 = (Map)list.get(i);
				List list2 = dt_menuservice.adminfindmenulist2(Integer.valueOf(String.valueOf(map2.get("menu_id"))));
				map2.put("list", list2);
				returnlist.add(map2);
			}
			map.put("menuList", returnlist);
			map.put("code", "100");
		}catch(Exception e){
			e.printStackTrace();
			map.put("code", "400");
			map.put("info", "查询失败");
		}
		return map;
	}
}









