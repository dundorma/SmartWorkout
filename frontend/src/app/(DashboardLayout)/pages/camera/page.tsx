'use client';
import { Box, Typography } from '@mui/material';
import PageContainer from '@/app/(DashboardLayout)/components/container/PageContainer';
import DashboardCard from '@/app/(DashboardLayout)/components/shared/DashboardCard';
import CameraAltIcon from '@mui/icons-material/CameraAlt';

const CameraPage = () => {
  return (
    <PageContainer title="Camera" description="This is the camera page">
      <DashboardCard title="Camera">
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            height: '500px',
            border: '1px dashed grey',
            borderRadius: '8px',
            position: 'relative',
            backgroundColor: '#f5f5f5',
          }}
        >
          <CameraAltIcon
            sx={{
              fontSize: 40,
              color: 'grey',
            }}
          />
          <Typography color="textSecondary">
            Camera View
          </Typography>
          <Box
            sx={{
              position: 'absolute',
              bottom: '10px',
              left: '10px',
              display: 'flex',
              alignItems: 'center',
            }}
          >
            <Box
              sx={{
                width: '24px',
                height: '24px',
                backgroundColor: '#fff',
                borderRadius: '50%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                border: '1px solid grey',
              }}
            >
              <CameraAltIcon sx={{ fontSize: 16, color: 'grey' }} />
            </Box>
          </Box>
          <Box
            sx={{
              position: 'absolute',
              bottom: '10px',
              right: '10px',
              display: 'flex',
              alignItems: 'center',
            }}
          >
            <Box
              sx={{
                width: '24px',
                height: '24px',
                backgroundColor: '#fff',
                borderRadius: '50%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                border: '1px solid grey',
                marginRight: '8px',
              }}
            >
              <Typography sx={{ fontSize: 12, color: 'grey' }}>⚙️</Typography>
            </Box>
            <Box
              sx={{
                width: '24px',
                height: '24px',
                backgroundColor: '#fff',
                borderRadius: '50%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                border: '1px solid grey',
              }}
            >
              <Typography sx={{ fontSize: 12, color: 'grey' }}>🔲</Typography>
            </Box>
          </Box>
        </Box>
      </DashboardCard>
    </PageContainer>
  );
};

export default CameraPage;
