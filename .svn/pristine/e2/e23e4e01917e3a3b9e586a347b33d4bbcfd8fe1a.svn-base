package com.hd.microblog.web.controller.code;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
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
import java.util.Random;

import javax.imageio.ImageIO;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import net.sf.json.JSONObject;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;

import com.hd.microblog.util.fileupload;
import com.sun.image.codec.jpeg.JPEGCodec;
import com.sun.image.codec.jpeg.JPEGImageEncoder;

@Controller
public class UploadfileController {
	
	//上传文件
	@RequestMapping(value = "/uploadfile", produces = "application/json; charset=utf-8")
	@ResponseBody
	public JSONObject uploadfile(HttpServletRequest request, HttpServletResponse resp,@RequestParam("file") MultipartFile filePath) throws IOException {
		HttpSession session = request.getSession();
		resp.setHeader("Access-Control-Allow-Origin", "*");
		resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
		JSONObject jobj = new JSONObject();
		try {
			fileupload upload = new fileupload();
			String loadpath = request.getSession().getServletContext().getRealPath("/") + "..//uploadfile" + File.separator;
			File filePath2 = upload.saveAttachFile(filePath, loadpath,true);
			System.out.println("name:"+filePath2.getName());
			jobj.accumulate("recode", 100);
			jobj.accumulate("filepath", filePath2.getName());
		
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
			jobj.accumulate("recode", "400");
			jobj.accumulate("reobj", "系统错误");
			jobj.accumulate("restr", "系统错误");
		}
		return jobj;
		
	}
	//上传图片
	@RequestMapping(value = "/uploadfile2", produces = "application/json; charset=utf-8")
	@ResponseBody
	public JSONObject uploadfile2(HttpServletRequest request, HttpServletResponse resp,@RequestParam("file") MultipartFile filePath) throws IOException {
		HttpSession session = request.getSession();
		resp.setHeader("Access-Control-Allow-Origin", "*");
		resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
		JSONObject jobj = new JSONObject();
		try {
			fileupload upload = new fileupload();
			String loadpath = request.getSession().getServletContext().getRealPath("/") + "..//upload" + File.separator;
			File filePath2 = upload.saveAttachFile(filePath, loadpath,true);
			System.out.println("name:"+filePath2.getName());
			jobj.accumulate("recode", 100);
			jobj.accumulate("filepath", filePath2.getName());
		
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
			jobj.accumulate("recode", "400");
			jobj.accumulate("reobj", "系统错误");
			jobj.accumulate("restr", "系统错误");
		}
		return jobj;
	}
	//上传水印图片
	@RequestMapping(value = "/uploadfile3", produces = "application/json; charset=utf-8")
	@ResponseBody
	public JSONObject uploadfile3(HttpServletRequest request, HttpServletResponse resp,@RequestParam("file") MultipartFile filePath) throws IOException {
		HttpSession session = request.getSession();
		resp.setHeader("Access-Control-Allow-Origin", "*");
		resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
		JSONObject jobj = new JSONObject();
		try {
			fileupload upload = new fileupload();
			String loadpath = request.getSession().getServletContext().getRealPath("/") + "..//upload" + File.separator;
			File filePath2 = upload.saveAttachFile(filePath, loadpath,true);
			System.out.println("name:"+filePath2.getName());
			//加水印
			String loadpath2 = request.getSession().getServletContext().getRealPath("/") + "..//video" + File.separator;
			InputStream imagein = new FileInputStream(loadpath+"/"+filePath2.getName());
            InputStream imagein2 = new FileInputStream(loadpath2+"/"+"sy.png");
            BufferedImage image = ImageIO.read(imagein);
            BufferedImage image2 = ImageIO.read(imagein2);
            Graphics g = image.getGraphics();
            g.drawImage(image2, image.getWidth() - image2.getWidth(), image.getHeight() - image2.getHeight(),
                    image2.getWidth(), image2.getHeight(), null);//坐标X，Y，宽，高
            OutputStream outImage = new FileOutputStream(loadpath+"/"+filePath2.getName());
            JPEGImageEncoder enc = JPEGCodec.createJPEGEncoder(outImage);
            enc.encode(image);
            imagein.close();
            imagein2.close();
            outImage.close();
			
			jobj.accumulate("recode", 100);
			jobj.accumulate("filepath", filePath2.getName());
			
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
			jobj.accumulate("recode", "400");
			jobj.accumulate("reobj", "系统错误");
			jobj.accumulate("restr", "系统错误");
		}
		return jobj;
	}	
	//图片查看
	@RequestMapping(value = "/upload/{imgid:.+}")
	public void download(@PathVariable("imgid")String fileid,HttpServletRequest request,
			HttpServletResponse response) throws UnsupportedEncodingException{
		
		response.setCharacterEncoding("utf-8");
		request.setCharacterEncoding("utf-8");
		
		try{
			String path = request.getSession().getServletContext()
					.getRealPath("/") +  "..//upload";
			
			String filepath = path+"//" + fileid;
			
			response.setHeader("Cache-Control", "no-store");
			response.setHeader("Pragma", "no-cache");
			response.setDateHeader("Expires", 0);
			
			ServletOutputStream out = response.getOutputStream();
			FileInputStream inputStream = new FileInputStream(filepath);
		    int n = 0;
		    byte b[] = new byte[1024];  
		    while ((n = inputStream.read(b)) != -1) {
		       	out.write(b, 0, n);
		    }
		    inputStream.close();
			out.flush();
			out.close();
		} catch(RuntimeException e){
			e.printStackTrace();
		} catch(Exception e){
			e.printStackTrace();
		}
	}
	//图片查看2
	@RequestMapping(value = "/uploadfile/{imgid:.+}")
	public void download2(@PathVariable("imgid")String fileid,HttpServletRequest request,
			HttpServletResponse response) throws UnsupportedEncodingException{
		
		response.setCharacterEncoding("utf-8");
		request.setCharacterEncoding("utf-8");
		
		try{
			String path = request.getSession().getServletContext()
					.getRealPath("/") +  "..//uploadfile";
			
			String filepath = path+"//" + fileid;
			
			response.setHeader("Cache-Control", "no-store");
			response.setHeader("Pragma", "no-cache");
			response.setDateHeader("Expires", 0);
			
			ServletOutputStream out = response.getOutputStream();
			FileInputStream inputStream = new FileInputStream(filepath);
		    int n = 0;
		    byte b[] = new byte[1024];  
		    while ((n = inputStream.read(b)) != -1) {
		       	out.write(b, 0, n);
		    }
		    inputStream.close();
			out.flush();
			out.close();
		} catch(RuntimeException e){
			e.printStackTrace();
		} catch(Exception e){
			e.printStackTrace();
		}
	}
}
