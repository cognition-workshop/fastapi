import { useState, useRef } from 'react'
import { Upload, Download, CheckCircle, AlertCircle, Loader2 } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Progress } from '@/components/ui/progress'
import { Alert, AlertDescription } from '@/components/ui/alert'

interface JobStatus {
  status: 'processing' | 'completed' | 'error'
  progress: number
  outputs?: {
    [key: string]: {
      filename: string
      quality: string
      path: string
    }
  }
  error?: string
  original_filename?: string
}

function App() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null)
  const [jobId, setJobId] = useState<string | null>(null)
  const [jobStatus, setJobStatus] = useState<JobStatus | null>(null)
  const [isUploading, setIsUploading] = useState(false)
  const fileInputRef = useRef<HTMLInputElement>(null)

  const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

  const handleFileSelect = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (file && file.type.startsWith('video/')) {
      setSelectedFile(file)
      setJobId(null)
      setJobStatus(null)
    } else {
      alert('Please select a valid video file')
    }
  }

  const uploadVideo = async () => {
    if (!selectedFile) return

    setIsUploading(true)
    const formData = new FormData()
    formData.append('file', selectedFile)

    try {
      const response = await fetch(`${API_URL}/encode`, {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        throw new Error('Upload failed')
      }

      const result = await response.json()
      setJobId(result.job_id)
      pollJobStatus(result.job_id)
    } catch (error) {
      console.error('Upload error:', error)
      alert('Upload failed. Please try again.')
    } finally {
      setIsUploading(false)
    }
  }

  const pollJobStatus = async (id: string) => {
    const poll = async () => {
      try {
        const response = await fetch(`${API_URL}/status/${id}`)
        if (response.ok) {
          const status = await response.json()
          setJobStatus(status)
          
          if (status.status === 'processing') {
            setTimeout(poll, 2000)
          }
        }
      } catch (error) {
        console.error('Status polling error:', error)
      }
    }
    poll()
  }

  const downloadVideo = (quality: string) => {
    if (jobId) {
      window.open(`${API_URL}/download/${jobId}/${quality}`, '_blank')
    }
  }

  const resetUpload = () => {
    setSelectedFile(null)
    setJobId(null)
    setJobStatus(null)
    if (fileInputRef.current) {
      fileInputRef.current.value = ''
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-4xl mx-auto px-4">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">Video Encoder</h1>
          <p className="text-lg text-gray-600">Upload a video and get it encoded in multiple quality levels</p>
        </div>

        <Card className="mb-6">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Upload className="w-5 h-5" />
              Upload Video
            </CardTitle>
            <CardDescription>
              Select a video file to encode into 360p, 720p, and 1080p quality levels
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <input
                  ref={fileInputRef}
                  type="file"
                  accept="video/*"
                  onChange={handleFileSelect}
                  className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
                />
              </div>
              
              {selectedFile && (
                <div className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                  <div>
                    <p className="font-medium">{selectedFile.name}</p>
                    <p className="text-sm text-gray-500">
                      {(selectedFile.size / (1024 * 1024)).toFixed(2)} MB
                    </p>
                  </div>
                  <div className="flex gap-2">
                    <Button onClick={uploadVideo} disabled={isUploading}>
                      {isUploading ? (
                        <>
                          <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                          Uploading...
                        </>
                      ) : (
                        'Start Encoding'
                      )}
                    </Button>
                    <Button variant="outline" onClick={resetUpload}>
                      Clear
                    </Button>
                  </div>
                </div>
              )}
            </div>
          </CardContent>
        </Card>

        {jobStatus && (
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                {jobStatus.status === 'completed' && <CheckCircle className="w-5 h-5 text-green-500" />}
                {jobStatus.status === 'error' && <AlertCircle className="w-5 h-5 text-red-500" />}
                {jobStatus.status === 'processing' && <Loader2 className="w-5 h-5 animate-spin text-blue-500" />}
                Encoding Status
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {jobStatus.status === 'processing' && (
                  <div>
                    <div className="flex justify-between text-sm mb-2">
                      <span>Processing...</span>
                      <span>{jobStatus.progress}%</span>
                    </div>
                    <Progress value={jobStatus.progress} className="w-full" />
                  </div>
                )}

                {jobStatus.status === 'error' && (
                  <Alert variant="destructive">
                    <AlertCircle className="h-4 w-4" />
                    <AlertDescription>
                      {jobStatus.error || 'An error occurred during encoding'}
                    </AlertDescription>
                  </Alert>
                )}

                {jobStatus.status === 'completed' && jobStatus.outputs && (
                  <div>
                    <Alert className="mb-4">
                      <CheckCircle className="h-4 w-4" />
                      <AlertDescription>
                        Video encoding completed successfully! Download your files below.
                      </AlertDescription>
                    </Alert>
                    
                    <div className="grid gap-3">
                      {Object.entries(jobStatus.outputs).map(([quality, output]) => (
                        <div key={quality} className="flex items-center justify-between p-3 border rounded-lg">
                          <div>
                            <p className="font-medium">{output.quality} Quality</p>
                            <p className="text-sm text-gray-500">{output.filename}</p>
                          </div>
                          <Button onClick={() => downloadVideo(quality)} size="sm">
                            <Download className="w-4 h-4 mr-2" />
                            Download
                          </Button>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  )
}

export default App
