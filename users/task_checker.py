from .models import AssignedTasks, UserDetails
from consent.models import UserConsent
from django.conf import settings
from django.contrib.auth.models import User
from main.models import Tasks
from ran.models import RanOrder
from spn.models import SpnPictureSet, SpnResponse
import os, glob



# FOR EACH TASK ONE SHOULD DEFINE A FINISHED-TASK-CHECKER. 
# Most tasks have a finish form as the last template view. 
# Clicking the "finish" button on the form will mark the 
# appropriate AssignedTask as complete. But if the user 
# closes his/her browser without clicking the finish button
# then actually finished tasks will continue to appear as
# incomplete in the database.
#
# The complete_checker() function is called each time a
# user loads his/her profile.


def complete_checker(USER):
	users_assignments = AssignedTasks.objects.filter(user_id=USER.id, complete=False)
	try:
		UD = UserDetails.objects.get(user=USER)
	except:
		UD = None
	URG = None
	if UD:
		URG = UD.research_group.target_lang_short_name
	for ass in users_assignments:

		print(ass.task)

		if ass.task.task == "Consent":
			#print('  ', ass.task.model_name)
			try:
				u_consent = UserConsent.objects.get(user=USER)
				if u_consent:
					ass.complete = True
					ass.save()
			except:
				print(f"{USER.username} has not consented")


		if ass.task.task == "User Details":
			#print('  ', ass.task.model_name)
			try:
				u_details = UserDetails.objects.get(user_id=USER.id)
				if u_details:
					ass.complete = True
					ass.save()
			except:
				print(f"{USER.username} has not provided his/her details'")

		if ass.task.url_name == 'questionnaire-welcome':
			print("  ~Erməgərrrd, there's no task checker for the questionnaires yet :|")

		if ass.task.task == "Automated Picture Naming":
			#print('  ', ass.task.model_name)
			try:
				ROobject = RanOrder.objects.get(user=USER)
			except:
				ROobject = None

			if ROobject:
				last_r_block = ROobject.block_6.strip('[]')
				last_r_stim = last_r_block.split(', ')[-1].strip("'")


				if glob.glob(f"{settings.MEDIA_ROOT}/recorded-audio/RAN-b6-{last_r_stim}_{URG}_{USER.id}_*.wav"):
					ass.complete = True 
					ass.save()

				else:
					print(f'  ~{USER.username} has started the RAN task but not finished it. The file RAN-b6-{last_r_stim}_{URG}_{USER.id}_*.wav does not exist.')
			else:
				print(f'  ~{USER.username} has not started the RAN task.')

		if ass.task.url_name == 'spn-welcome':
			pic_set = SpnPictureSet.objects.get(slug=ass.task.url_arg)
			pic_set_block = pic_set.pictures.all().order_by('sort_order')
			num_block_stim = len(pic_set_block)
			num_block_resp = len(SpnResponse.objects.filter(task=ass.task, user=USER))


			if num_block_resp == 0:
				print(f"  ~{USER.username} has not started the SPN task '{pic_set.name}' yet.")
			elif num_block_resp == num_block_stim:
				print(f"  ~{USER.username} is done with SPN task '{pic_set.name}'. Fixing that in the database.")
				ass.complete = True
				ass.save()
				#print("  ~~I jus' saved yo' ass!~~")
			else:
				print(f"  ~{USER.username} started SPN '{pic_set.name}', but did not finish. Fix that ish, yo")




