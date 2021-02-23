LoadISISNexus(Filename=r'\\isis.cclrc.ac.uk\inst$\ndxoffspec\instrument\data\cycle_18_1\OFFSPEC00046999.nxs', OutputWorkspace='46999')
LoadNexus(Filename=r'\\isis.cclrc.ac.uk\inst$\ndxoffspec\instrument\data\cycle_18_1\OFFSPEC00046992.nxs', OutputWorkspace='TOF_46992')
LoadNexus(Filename=r'\\isis.cclrc.ac.uk\inst$\ndxoffspec\instrument\data\cycle_18_1\OFFSPEC00046993.nxs', OutputWorkspace='TOF_46993')
LoadNexus(Filename=r'\\isis.cclrc.ac.uk\inst$\ndxoffspec\instrument\data\cycle_18_1\OFFSPEC00046994.nxs', OutputWorkspace='TOF_46994')

# Child algorithms of ReflectometryReductionOneAuto
SpecularReflectionPositionCorrect(InputWorkspace='TOF_46992', TwoTheta=1, DetectorComponentName='WLSFDetector', OutputWorkspace='__TMP000001B29A437BE0')

## Child algorithms of ReflectometryReductionOne
ConvertUnits(InputWorkspace='__TMP000001B29A437BE0', OutputWorkspace='__TMP000001B29A43C050', Target='Wavelength', AlignBins=True)
CropWorkspace(InputWorkspace='__TMP000001B29A437BE0', OutputWorkspace='__TMP000001B29A43C4E0', StartWorkspaceIndex=1, EndWorkspaceIndex=1)
ConvertUnits(InputWorkspace='__TMP000001B29A43C4E0', OutputWorkspace='__TMP000001B29A43D720', Target='Wavelength', AlignBins=True)
CalculateFlatBackground(InputWorkspace='__TMP000001B29A43D720', OutputWorkspace='__TMP000001B29A435BF0', StartX=15, EndX=20)
Integration(InputWorkspace='__TMP000001B29A435BF0', OutputWorkspace='__TMP000001B21108ACD0', RangeLower=2, RangeUpper=14)
Divide(LHSWorkspace='__TMP000001B29A43C050', RHSWorkspace='__TMP000001B21108ACD0', OutputWorkspace='__TMP000001B211085F40')

### Child algorithms of CreateTransmissionWorkspace
GroupDetectors(InputWorkspace='46999', OutputWorkspace='__TMP000001B211084870', GroupingPattern='389-419')
ConvertUnits(InputWorkspace='__TMP000001B211084870', OutputWorkspace='__TMP000001B21108ACD0', Target='Wavelength', AlignBins=True)
CropWorkspace(InputWorkspace='46999', OutputWorkspace='__TMP000001B2110843E0', StartWorkspaceIndex=1, EndWorkspaceIndex=1)
ConvertUnits(InputWorkspace='__TMP000001B2110843E0', OutputWorkspace='__TMP000001B2110831A0', Target='Wavelength', AlignBins=True)
CalculateFlatBackground(InputWorkspace='__TMP000001B2110831A0', OutputWorkspace='__TMP000001B211084870', StartX=15, EndX=20)
Integration(InputWorkspace='__TMP000001B211084870', OutputWorkspace='__TMP000001B21108DF00', RangeLower=2, RangeUpper=14)
Divide(LHSWorkspace='__TMP000001B21108ACD0', RHSWorkspace='__TMP000001B21108DF00', OutputWorkspace='__TMP000001B2110831A0')
CropWorkspace(InputWorkspace='__TMP000001B2110831A0', OutputWorkspace='', XMin=2, XMax=14)
### End of child algorithms of CreateTransmissionWorkspace

RebinToWorkspace(WorkspaceToRebin='__TMP000001B21108ACD0', WorkspaceToMatch='__TMP000001B211085F40', OutputWorkspace='__TMP000001B2110831A0')
Divide(LHSWorkspace='__TMP000001B211085F40', RHSWorkspace='__TMP000001B2110831A0', OutputWorkspace='__TMP000001B211084870')
CropWorkspace(InputWorkspace='__TMP000001B21108ACD0', OutputWorkspace='', XMin=2.2706240905191248, XMax=12.522721109543975)
ConvertUnits(InputWorkspace='__TMP000001B2110831A0', OutputWorkspace='IvsQ_46992', Target='MomentumTransfer')
## End of child algorithms of ReflectometryReductionOne

Rebin(InputWorkspace='__TMP000001B2110843E0', OutputWorkspace='IvsQ_binned_46992', Params='0.00879554,-0.03,0.0485021')
# End of child algorithms of ReflectometryReductionOneAuto

ReflectometryReductionOneAuto(InputWorkspace='TOF_46993', SummationType='SumInQ', ReductionType='NonFlatSample', ProcessingInstructions='390-420', ThetaIn=1.5, FirstTransmissionRun='46999', MomentumTransferMin=0.024461616931990889, MomentumTransferStep=0.029999999999999999, MomentumTransferMax=0.15799278359086491, ScaleFactor=1, OutputWorkspaceBinned='IvsQ_binned_46993', OutputWorkspace='IvsQ_46993', OutputWorkspaceWavelength='IvsLam_46993')
ReflectometryReductionOneAuto(InputWorkspace='TOF_46994', SummationType='SumInQ', ReductionType='NonFlatSample', ProcessingInstructions='390-420', ThetaIn=2.5, FirstTransmissionRun='46999', MomentumTransferMin=0.040126133459340192, MomentumTransferStep=0.029999999999999999, MomentumTransferMax=0.26776949075729722, ScaleFactor=1, OutputWorkspaceBinned='IvsQ_binned_46994', OutputWorkspace='IvsQ_46994', OutputWorkspaceWavelength='IvsLam_46994')
Stitch1DMany(InputWorkspaces='IvsQ_46992,IvsQ_46993,IvsQ_46994', OutputWorkspace='IvsQ_46992_46993_46994', Params='-0.03', OutScaleFactors='0.125265,0.0526235')
