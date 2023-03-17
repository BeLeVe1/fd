package com.hd.microblog.web.controller.code;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;

import com.hd.microblog.web.controller.code.ImageUtil;

/**
 * 图片上传，有可能前端也要上传图片，所以没有以/admin管理
 * 
 * @author 程高伟
 * @date 2017年3月27日 下午5:41:11
 */
@Controller
public class FileUploadController {
    /**
     * summernote图片上传处理，可以处理同时上传多张图片的情形
     * 
     * @param files
     * @param request
     * @return
     * @throws IOException
     */
    @RequestMapping(value = "/uploadImage", method = RequestMethod.POST, produces = "application/json;charset=utf8")
    @ResponseBody
    public List uploadMultipleFileHandler(@RequestParam("file") MultipartFile[] files, HttpServletRequest request)
            throws IOException {
        List list = new ArrayList<>();
        for (MultipartFile file : files) {
        	String loadpath = request.getSession().getServletContext().getRealPath("/") + "..//upload" + File.separator;
        	String url = ImageUtil.saveImage(request, file, loadpath , "upload/");
        	Map map = new HashMap();
        	map.put("url", url);
            //map.put("fileName", file.getOriginalFilename());
            list.add(map);
        }
        System.out.println("===="+list);
        return list;
    }
    @RequestMapping(value = "/uploadImage2", method = RequestMethod.POST, produces = "application/json;charset=utf8")
    @ResponseBody
    public List uploadMultipleFileHandler2(@RequestParam("file") MultipartFile[] files, HttpServletRequest request)
            throws IOException {
        List list = new ArrayList<>();
        for (MultipartFile file : files) {
        	String loadpath = request.getSession().getServletContext().getRealPath("/") + "..//uploadfile" + File.separator;
        	String url = ImageUtil.saveImage(request, file, loadpath , "uploadfile/");
        	Map map = new HashMap();
        	map.put("url", url);
            //map.put("fileName", file.getOriginalFilename());
            list.add(map);
        }
        System.out.println("===="+list);
        return list;
    }
	/*
	 * public class Image { // 图片上传后的路径 private String url; // 上传图片的名称 private
	 * String fileName;
	 * 
	 * public String getUrl() { return url; }
	 * 
	 * public void setUrl(String url) { this.url = url; }
	 * 
	 * public String getFileName() { return fileName; }
	 * 
	 * public void setFileName(String fileName) { this.fileName = fileName; }
	 * 
	 * @Override public String toString() { return "Image [url=" + url +
	 * ", fileName=" + fileName + "]"; }
	 * 
	 * }
	 */

}