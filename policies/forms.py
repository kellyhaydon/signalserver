from django import forms
from .models import Policy, Operation

SIGNALS = (
    ('None', 'None'),
    ('lavfi.signalstats.BRNG', 'BRNG'),
    ('lavfi.cropdetect.y2', 'Crop Bottom'),
    ('lavfi.cropdetect.y1', 'Crop Top'),
    ('lavfi.cropdetect.x1', 'Crop Left'),
    ('lavfi.cropdetect.x2', 'Crop Right'),
    ('lavfi.cropdetect.h', 'Crop Height'),
    ('lavfi.cropdetect.w', 'Crop Width'),
    ('lavfi.cropdetect.x', 'Crop X'),
    ('lavfi.cropdetect.y', 'Crop Y'),
    ('lavfi.signalstats.HUEAVG', 'HUE AVG'),
    ('lavfi.signalstats.HUEMED', 'HUE MED'),
    ('lavfi.psnr.mse_avg', 'MSEf Avg'),
    ('lavfi.psnr.mse.u', 'MSEf U'),
    ('lavfi.psnr.mse.v', 'MSEf V'),
    ('lavfi.psnr.mse.y', 'MSEf Y'),
    ('lavfi.psnr.psnr_avg', 'PSNRf Avg'),
    ('lavfi.psnr.psnr.u', 'PSNRf U'),
    ('lavfi.psnr.psnr.v', 'PSNRf V'),
    ('lavfi.psnr.psnr.y', 'PSNRf Y'),
    ('lavfi.r128.I', 'R128.I'),
    ('lavfi.r128.LRA', 'R128.LRA'),
    ('lavfi.r128.LRA.high', 'R28.LRA.high'),
    ('lavfi.r128.LRA.low', 'R128.LRA.low'),
    ('lavfi.r128.M', 'R128.M'),
    ('lavfi.r128.S', 'R128.S'),
    ('lavfi.signalstats.SATAVG', 'SAT AVG'),
    ('lavfi.signalstats.SATHIGH', 'SAT HIGH'),
    ('lavfi.signalstats.SATLOW', 'SAT LOW'),
    ('lavfi.signalstats.SATMAX', 'SAT MAX'),
    ('lavfi.signalstats.SATMIN', 'SAT MIN'),
    ('lavfi.signalstats.TOUT', 'TOUT'),
    ('lavfi.signalstats.UAVG', 'U AVG'),
    ('lavfi.signalstats.UDIF', 'U DIF'),
    ('lavfi.signalstats.UHIGH', 'U HIGH'),
    ('lavfi.signalstats.ULOW', 'U LOW'),
    ('lavfi.signalstats.UMAX', 'U MAX'),
    ('lavfi.signalstats.UMIN', 'U MIN'),
    ('lavfi.signalstats.VAVG', 'V AVG'),
    ('lavfi.signalstats.VDIF', 'V DIF'),
    ('lavfi.signalstats.VHIGH', 'V HIGH'),
    ('lavfi.signalstats.VLOW', 'V LOW'),
    ('lavfi.signalstats.VMAX', 'V MAX'),
    ('lavfi.signalstats.VMIN', 'V MIN'),
    ('lavfi.signalstats.VREP', 'VREP'),
    ('lavfi.signalstats.YAVG', 'Y AVG'),
    ('lavfi.signalstats.YDIF', 'Y DIF'),
    ('lavfi.signalstats.YHIGH', 'Y HIGH'),
    ('lavfi.signalstats.YLOW', 'Y LOW'),
    ('lavfi.signalstats.YMAX', 'Y MAX'),
    ('lavfi.signalstats.YMIN', 'Y MIN')
)
OPERATIONS = (
    ('average', 'average'),
    ('exceeds', 'exceeds'),
    ('average_difference', 'average_difference'),
)


class PolicyNameForm(forms.Form):
    policy_name = forms.CharField(label='Policy name', max_length=200)


#class UploadFileForm(forms.Form):
#    title = forms.CharField(max_length=50)
#    file_name = forms.CharField()


class PolicyForm(forms.Form):
    policy_name = forms.CharField(
        label='Policy name'
    )
    display_order = forms.IntegerField(
        label='Policy order', initial=0
    )


class OperationForm(forms.Form):
    signal_fields = forms.ChoiceField(choices=SIGNALS, required=True)
    operation_fields = forms.ChoiceField(
        choices=OPERATIONS,
        required=True,
        widget=forms.Select(attrs={"onChange": 'operationSelect(this)'})
    )
    second_signal_fields = forms.ChoiceField(
        choices=SIGNALS, required=False
    )
    cutoff_number = forms.IntegerField(
        label='Please enter the cut off number', initial=0
    )
    display_order = forms.IntegerField(
        label='Please enter the display order', initial=0
    )
