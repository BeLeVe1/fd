package com.hd.microblog.util;

import java.io.File;
import java.util.Date;

import javax.servlet.http.HttpServletRequest;

import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

public class fileupload {
	
	public File saveAttachFile(MultipartFile file,String loadpath,boolean IsNumname) {

		File file2 = null;
		// 判断文件是否为空
		if (!file.isEmpty()) {
			try {
				// 文件保存路径
				File filedir = new File(loadpath);
				if (!filedir.exists()) {
					filedir.mkdirs();
				}
				String filename = file.getOriginalFilename();
				if(IsNumname) {
					//生成文件名
					int sjcode = (int) (Math.random()*9000+1000);
					String order_code = String.valueOf(System.currentTimeMillis() / 1000)+sjcode;
					int point = filename.indexOf(".");
					filename = order_code + filename.substring(point, filename.length());
				}
				
				loadpath = loadpath + filename;
				// 转存文件
				file2 = new File(loadpath);
				file.transferTo(file2);

			} catch (Exception e) {
				e.printStackTrace();
				return file2;
			}
		}
		return file2;
	}

}
