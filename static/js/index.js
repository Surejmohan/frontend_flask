
var htm = '';

/*emailField.addEventListener('keyup', function (event) {
	isValidEmail = emailField.checkValidity();
	
	if ( isValidEmail ) {
	  okButton.disabled = false;
	} else {
	  okButton.disabled = true;
	}
  });
	
  okButton.addEventListener('click', function (event) {
	signUpForm.submit();
  });
*/
$("#captche").hide();
function codevalidate(){

	var v = grecaptcha.getResponse()
	console.log(v.length);
	if (v.length == 0){

		document.getElementById("captche").innerHTML = "Captcha code empty";
		$("#captche").show();
		return false;
	}
	else
	{
		$.post("mass.html");
		$("#captche").hide();
		signin.submit();
	}
	
}






function User()
{


htm = `
<h2 class="well" style="min-width: 320px;margin-top:2%; text-align: center;font-weight: bold;"id ="register" >Registration Form</h2>
<form action ="" method ="POST">
<div class="col-lg-12 ">
<div class=" col-xs-12 col-sm-6 col-md-9">


			<div class="row">
			<div class="col-xs-12 col-sm-6 form-group">
			<label><b>First Name &nbsp;<span style="color: red;">*</span></b></label>
			<input type="text" placeholder="Enter First Name" class="form-control" value="" pattern="([a-zA-Z]*)" title="It contains alphabets only"  required />
			</div>

			<div class="col-xs-12 col-sm-6 form-group">
			<label><b>Last Name &nbsp;<span style="color: red;">*</span></b></label>
			<input type="text" placeholder="Enter Last Name" class="form-control" value="" pattern="([a-zA-Z]*)" title="It contains alphabets only"  required />
			</div>
			</div>					


			<div class="row">
			<div class="col-xs-12 col-sm-6 col-md-9 form-group">
			<label><b>User Name &nbsp;<span style="color: red;">*</span></b></label>
			<input type="text" placeholder="Enter User Name " class="form-control" value="" pattern="([0-9a-zA-Z]*)" title="It contain letters and numbers only"  required/>
			</div>
			</div>
			
			<div class="row">
			<div class="col-xs-12 col-sm-6 form-group">
			<label><b>Password &nbsp;<span style="color: red;">*</span></b></label>
			<input type="password" placeholder="Enter Password *" class="form-control"  maxlength="12"  pattern="[0-9a-zA-Z].{8,}" title="It includes  numbers , uppercase,lowercase letter, and at least 8 or more characters required (Max length:12)" required >
			</div>	
			

			
			<div class="col-sm-6 form-group">
			<label><b>Confirm password &nbsp;<span style="color: red;">*</span></b></label>
			<input type="password" placeholder="Enter Confirm Password *" class="form-control" value=""  maxlength="12" pattern="[0-9a-zA-Z].{8,}" title="It includes  numbers , uppercase,lowercase letter, and at least 8 or more characters required (Max length:12)" required />
			</div>	
			</div>	
	
			<div class="row">					
			<div class="col-sm-4 form-group col-xs-12 col-sm-6 ">
			<label><b>Mobile Number &nbsp;<span style="color: red;">*</span></b></label>
			<input type="tel" placeholder="Enter Mobile Number *" class="form-control" value=""  maxlength="10" pattern="[0-9]{10}" title="10 digit number" required />	</div>


			<div class="form-group col-sm-4 col-xs-12 col-sm-6 ">
			<label><b>Email Address &nbsp;<span style="color: red;">*</span></b></label>
			<input type="email" placeholder="Enter Email Address *" class="form-control" title="Valid email address" required />
			</div>	
			</div>

			<div class = "row">
			<div class="form-group col-xs-12 col-sm-6">
			<label><b>Address &nbsp;<span style="color: red;">*</span></b></label>
			<textarea placeholder="Enter Address Here.." rows="3" class="form-control"  title="It contains Alphabets and Numbers only"  required/></textarea>
			</div>	
			
			<div class="col-sm-4 form-group col-xs-12 col-sm-6 ">
			<label><b>City &nbsp;<span style="color: red;">*</span></b></label>
			<input type="text" placeholder="Enter City Name Here.." class="form-control" pattern="([a-zA-Z]*)" title="It contains Alphabets only"  required />
			</div>	
			</div>

			<div class = "row">
			<div class="col-sm-4 form-group col-xs-12 col-sm-6 ">
			<label><b>State &nbsp;<span style="color: red;">*</span></b></label>
			<input type="text" placeholder="Enter State Name Here.." class="form-control" pattern="([a-zA-Z]*)" title="It contains Alphabets only"  required />
			</div>	
			<div class="col-sm-4 form-group col-xs-12 col-sm-6 ">
			<label><b>Zip &nbsp;<span style="color: red;">*</span></b></label>
			<input type="text" placeholder="Enter Zip Code Here.." class="form-control" pattern="[0-9]{6}" title="It contains 6 digits only" maxlength="6" required  />
			</div>
			</div>		
					
			<div class="row">
			<div class="form-group"><br>
			<label class=" control-label" for="filebutton"><b>Upload Any proof &nbsp;<span style="color: red;">*</span></b></label>
			<div class="col-xs-12 col-sm-6 col-md-9">
			<input name="filebutton" class="input-file" id="filebutton" type="file" required>
			</div>
			</div>
			</div>
		</div>
	</div>

					<br>
						<div class="col-sm-4 container-fluid col-xs-12 col-sm-6"style="margin:auto auto auto auto; min-width: 300px; max-width: 85%; border-radius: 7%;"><br>
		  <label><b style="font-size: 27px;">Instructions</b></label>
		  <br>
		  <ul style="text-align:left">
		  <li>Use this site for good and legal things only.Malpractises should be avoided.</li>
		  <li>The input image you uploaded should  be clear. Noisy or incorrect image should lead to incorrect result. That willl not be our fault.</li>
		  <li>All the information given should be correct and not illegaly created.</li>
		  <li>Creating fake missing cases and use this site for search that person is a crime.</li>
		  <li>Your personal information is completely encrypted and safe in our hand.</li>
		  </ul>
		<br>
		<br>
		</div> 
		<input type="checkbox" class="form-check-input position-static" id="userinstruct" value="done" required>
		&nbsp;<label class="form-check-label"> I have a Read the Instructions</label> &nbsp;<span style="color: red;">*</span><br><br><br>
		  
		 <br><br>
		 <span style="color: red;">* Required Fields</span><br><br>
		
						<button type="submit" id ="usersignup" style=" background-color:#2dc997;max-width: 50%;" class="btn btn-lg btn-info">Submit</button>	<br>
						</form>
						
  
						`

document.getElementById("user").innerHTML= htm;

}














function Authority()
{


htm = `<h2 class="well" style="min-width: 320px;margin-top:2%; text-align: center;font-weight: bold;"id ="authority" >Registration Form</h2>
<form action="" method = "POST">
<div class="col-lg-12 ">
<div class=" col-xs-12 col-sm-6 col-md-9">

						<div class="row">
						<div class="col-xs-12 col-sm-6 form-group">
							<label><b>First Name &nbsp;<span style="color: red;">*</span></b></label>
							<input type="text" placeholder="Enter First Name" class="form-control" value="" pattern="([a-zA-Z]*)" title="It contains alphabets only"  required />
						</div>
						<div class="col-xs-12 col-sm-6 form-group">
							<label><b>Last Name &nbsp;<span style="color: red;">*</span></b></label>
							<input type="text" placeholder="Enter Last Name" class="form-control" value="" pattern="([a-zA-Z]*)" title="It contains alphabets only"  required />
						</div>
						</div>			
						<div class="row">

						<div class="col-xs-12 col-sm-6 col-md-9 form-group">
						<label><b>User Name &nbsp;<span style="color: red;">*</span></b></label>
						<input type="text" placeholder="Enter User Name " class="form-control" value="" pattern="([0-9a-zA-Z]*)" title="It contain letters and numbers only"  required />
						</div>
						</div>
			
						<div class="row">
						<div class="col-xs-12 col-sm-6 form-group">
						<label><b>Password &nbsp;<span style="color: red;">*</span></b></label>
						<input type="password" placeholder="Enter Password *" class="form-control"  maxlength="12" pattern="[0-9a-zA-Z].{8,}" title="It includes  numbers , uppercase,lowercase letter, and at least 8 or more characters required (Max length:12)" required>
						</div>	
			

			
						<div class="col-sm-6 form-group">
						<label><b>Confirm password &nbsp;<span style="color: red;">*</span></b></label>
						<input type="password" placeholder="Enter Confirm Password *" class="form-control" value=""  maxlength="12" pattern="[0-9a-zA-Z].{8,}" title="It includes  numbers , uppercase,lowercase letter, and at least 8 or more characters required (Max length:12)" required />
						</div>	
						</div>	

						<div class="row">					
						<div class="col-sm-4 form-group col-xs-12 col-sm-6 ">
						<label><b>Mobile Number &nbsp;<span style="color: red;">*</span></b></label>
						<input type="tel" placeholder="Enter Mobile Number *" class="form-control" value=""  maxlength="10" pattern="[0-9]{10}" title="10 digit number" required >	</div>


						<div class="form-group col-sm-4 col-xs-12 col-sm-6 ">
						<label><b>Email Address &nbsp;<span style="color: red;">*</span></b></label>
						<input type="email" placeholder="Enter Email Address *" class="form-control" required>
						</div>	
						</div>

						<div class="row">
						<div class="form-group col-sm-4 col-xs-12 col-sm-6">
						<label for="job">Job Title:</label>&nbsp;

						<select id="job" required>
						  <option class="dropdown-item" value="">--select option--</option>
						  <option class="dropdown-item" value="Police">Police Force</option>
						  <option class="dropdown-item" value="RPF">RPF</option>
						  <option class="dropdown-item" value="Others">Others</option>
						
						</select>
						</div>
				
					<div class="form-group"><br>
					<label class=" control-label" for="filebutton"><b><span style="color: red;">*</span>Upload ID card Image</b></label>
					<div class="col-xs-12 col-sm-6 col-md-9">
					<input name="filebutton" class="input-file" id="filebutton" type="file" required>
					</div>
					</div>
					</div>


</div>
</div>
<div class="col-sm-4 form-group col-xs-12 col-sm-6"style="	margin:auto auto auto auto; min-width: 300px; max-width: 85%; border-radius: 7%;"><br>
<label><b style="font-size: 27px;">Instructions</b></label>
<br>
<ul style="text-align:left">
<li>Use this site for good and legal things only.Malpractises should be avoided.</li>
<li>The input image you uploaded should  be clear. Noisy or incorrect image should lead to incorrect result. That willl not be our fault.</li>
<li>All the information given should be correct and not illegaly created.</li>
<li>Creating fake missing cases and use this site for search that person is a crime.</li>
<li>Your personal information is completely encrypted and safe in our hand.</li>
</ul>
<br>
<br>
</div> 
<input type="checkbox" class="form-check-input position-static" id="instruct" value="done" required>
&nbsp;<label class="form-check-label"> I have a Read the Instructions</label>&nbsp;<span style="color: red;">*</span><br><br><br>

<br><br>
<span style="color: red;">* Required Fields</span><br><br>

			  <button type="submit" style="background-color:#2dc997;max-width: 50%;" class="btn btn-lg btn-info">Submit</button>	<br>
	
			  </form>
			  `

document.getElementById("authority").innerHTML= htm;

}

$("#but1").click(function () {

	$("#but1").hide();
	$("#but2").hide();
	$("#authority").hide();
	$("#user").show();

});

$("#but2").click(function () {

	$("#but1").hide();
	$("#but2").hide();
	$("#user").hide();
	$("#authority").show();
	
});


$("#but4").click(function () {

	$("#but1").show();
	$("#but2").show();
	$("#authority").hide();
	$("#user").hide();
	

});



