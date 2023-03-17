package com.hd.microblog.web.controller.code;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.EncodeHintType;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.client.j2se.MatrixToImageWriter;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.qrcode.decoder.ErrorCorrectionLevel;

@Controller
public class QrcodeController {
	
	/*@Autowired
	@Qualifier("dt_userService")
	private dt_userService dt_userservice;*/
	
	
	//小白二维码生成
	@RequestMapping(value = "/createxiaobaiqrcode", produces = "application/json; charset=utf-8")
	@ResponseBody
	public Map createxiaobaiqrcode(HttpServletRequest request, HttpServletResponse resp) throws IOException {
		resp.setHeader("Access-Control-Allow-Origin", "*");
		resp.setHeader("Access-Control-Allow-Methods", "GET,POST");
		
		Map map = new HashMap<String, String>();
		final int width = 400;
		final int height = 400;
		final String format = "png";
		final String content = "http://jikewangluo.cn/0yzzq/regist1.html?recode=8pPzh229&from=singlemessage";
		
		//定义二维码的参数
		HashMap hints = new HashMap();
		hints.put(EncodeHintType.CHARACTER_SET, "utf-8");
		hints.put(EncodeHintType.ERROR_CORRECTION, ErrorCorrectionLevel.M);
		hints.put(EncodeHintType.MARGIN, 2);
		
		//生成二维码
		try{
			//OutputStream stream = new OutputStreamWriter();
			BitMatrix bitMatrix = new MultiFormatWriter().encode(content, BarcodeFormat.QR_CODE, width, height, hints);
			Path file = new File("D:/1111.png").toPath();
			MatrixToImageWriter.writeToPath(bitMatrix, format, file);
			//MatrixToImageWriter.writeToStream(bitMatrix, format, stream);
			map.put("image", "1111.png");
			map.put("code", "100");
			map.put("info", "生成成功");
		}catch(Exception e){
			e.printStackTrace();
			map.put("code", "400");
			map.put("info", "系统错误");
		}
		return map;
	}
}
