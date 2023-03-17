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





@Controller
public class AdminloginController {
	
	@Autowired
	@Qualifier("dt_adminService")
	private dt_adminService dt_adminservice;
	
	
	//后台登录页面
	@RequestMapping("/adminlogin")
	public String admin(HttpServletRequest request, HttpServletResponse resp) 
			throws IOException {
		return "admin/login";
	}	
	//后台登录
	@RequestMapping(value = "/adminloginajax", method = { RequestMethod.POST }, produces = "application/json; charset=utf-8")
	@ResponseBody
	private Map loginAjax(HttpServletRequest request, String account, String password,
			String code) throws UnsupportedEncodingException {
		
		HttpSession session = request.getSession();
		Map returnmap = new HashMap();
		String passwordmd5 = MD5.MD5Encode("y7<LF5H2qgfIx]AD{6Yg"+MD5.MD5Encode(password, "UTF-8"), "UTF-8");
		List list = dt_adminservice.adminfindaccount(account);
		if(list!=null&&list.size()==1) {
			dt_admin admin = (dt_admin) list.get(0);
			if(admin.getPassword().equals(passwordmd5)) {
				if (code.equalsIgnoreCase(session.getAttribute("code").toString())) {
					session.setAttribute("admin", admin);
					returnmap.put("rcode", "100");
					returnmap.put("rinfo", "成功");
				}else {
					returnmap.put("rcode", "400");
					returnmap.put("rinfo", "验证码错误");
				}
			}else {
				returnmap.put("rcode", "400");
				returnmap.put("rinfo", "密码错误");
			}
		}else {
			returnmap.put("rcode", "400");
			returnmap.put("rinfo", "账号错误");
		}
		return returnmap;
	}	
	
}









