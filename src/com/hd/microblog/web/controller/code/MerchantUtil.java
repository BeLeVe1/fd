package com.hd.microblog.web.controller.code;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.sql.SQLException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import sun.misc.BASE64Decoder;

@Controller
public class MerchantUtil {
	
	@RequestMapping(value = "merchantupload", method = RequestMethod.POST)
	public @ResponseBody
	ResultInfo<String> upload(HttpServletRequest request,HttpServletResponse response,
			@RequestParam("file")String fileData) throws IOException {
		
		ResultInfo<String> info = new ResultInfo<String>();
		
		try{
			// 1 得到上传服务器的路径
			String path = request.getSession().getServletContext()
								.getRealPath("/") +  "..//upload";
			// 2 新建文件目录
			File file = new File(path);
			if (!file.exists()) {
				file.mkdir();
			}
			
			String ext = subStringBetween(fileData, "data:image/", ";"); 
			
			String fileId =new SimpleDateFormat("yyyyMMddHHmmssSSS").format(new Date())+ "." + ext;
			  
			path += "//" + fileId;
			
		Pattern pattern = Pattern.compile("^data:image/[^;]*;base64,(.*)$");  
		Matcher matcher = pattern.matcher(fileData);
		if (matcher.find()){
			 String base64ImgData = matcher.group(1);  
	         convertBase64DataToImage(base64ImgData, path);
		}
		info.setErrorCode(0);
		info.setResult(fileId);
		return info;
		} catch(RuntimeException e){
			e.printStackTrace();
		} catch (Exception e){
			e.printStackTrace();
		} 
		return ResultInfo.getIllegalData();
	}
	private void convertBase64DataToImage(String base64ImgData,String filePath) throws IOException {  
        BASE64Decoder d = new BASE64Decoder();  
        byte[] bs = d.decodeBuffer(base64ImgData);  
        FileOutputStream os = new FileOutputStream(filePath);  
        os.write(bs);  
        os.close();  
	}  
	private String subStringBetween(String sour , String start, String end){
		String result = null;
		if (sour!=null&&start!=null&&end!=null){
			int s = sour.indexOf(start);
			int e = sour.indexOf(end);
			if(s>-1&&e>-1&&e>=s){
				result = sour.substring(s + start.length(), e);
			}
		}
		if (result == null)
			result = "jpg";
		return result;
	}
}
